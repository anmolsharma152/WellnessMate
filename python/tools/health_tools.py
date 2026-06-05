"""
Custom Tools for WellnessMate Agents
Health calculation tools used by the CrewAI agents
"""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Literal


# ── BMI Calculator ────────────────────────────────────────────────────────────


class BMIInput(BaseModel):
    weight_kg: float = Field(..., description="Weight in kilograms")
    height_cm: float = Field(..., description="Height in centimetres")


class BMICalculatorTool(BaseTool):
    name: str = "BMI Calculator"
    description: str = (
        "Calculates Body Mass Index (BMI) from weight and height, "
        "and returns the BMI value with its WHO classification."
    )
    args_schema: Type[BaseModel] = BMIInput

    def _run(self, weight_kg: float, height_cm: float) -> str:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m**2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25.0:
            category = "Normal weight"
        elif bmi < 30.0:
            category = "Overweight"
        else:
            category = "Obese"

        return (
            f"BMI: {bmi:.1f} — {category} "
            f"(WHO classification: <18.5 Underweight | 18.5–24.9 Normal | "
            f"25–29.9 Overweight | ≥30 Obese)"
        )


# ── TDEE Calculator ───────────────────────────────────────────────────────────


class TDEEInput(BaseModel):
    weight_kg: float = Field(..., description="Weight in kilograms")
    height_cm: float = Field(..., description="Height in centimetres")
    age: int = Field(..., description="Age in years")
    gender: Literal["male", "female"] = Field(
        ..., description="Biological sex: 'male' or 'female'"
    )
    activity_level: Literal[
        "sedentary", "light", "moderate", "active", "very_active"
    ] = Field(
        ...,
        description=(
            "Activity level: "
            "sedentary (desk job, no exercise), "
            "light (1-3 days/week), "
            "moderate (3-5 days/week), "
            "active (6-7 days/week), "
            "very_active (physical job + training)"
        ),
    )


class TDEECalculatorTool(BaseTool):
    name: str = "TDEE Calculator"
    description: str = (
        "Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation "
        "and Total Daily Energy Expenditure (TDEE) based on activity level. "
        "Use this before creating any meal plan."
    )
    args_schema: Type[BaseModel] = TDEEInput

    def _run(
        self,
        weight_kg: float,
        height_cm: float,
        age: int,
        gender: str,
        activity_level: str,
    ) -> str:
        # Mifflin-St Jeor Equation
        if gender.lower() == "male":
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

        multipliers = {
            "sedentary": 1.200,
            "light": 1.375,
            "moderate": 1.550,
            "active": 1.725,
            "very_active": 1.900,
        }
        tdee = bmr * multipliers.get(activity_level.lower(), 1.55)

        return (
            f"BMR: {bmr:.0f} kcal/day | "
            f"TDEE ({activity_level}): {tdee:.0f} kcal/day | "
            f"Weight loss target: {tdee - 500:.0f} kcal/day | "
            f"Muscle gain target: {tdee + 300:.0f} kcal/day"
        )


# ── Micro-Habit Suggestor ─────────────────────────────────────────────────────


class MicroHabitInput(BaseModel):
    goal: str = Field(
        ...,
        description="The user's wellness goal (e.g. 'reduce stress', 'sleep better', 'lose weight')",
    )
    available_minutes_per_day: int = Field(
        ...,
        description="How many minutes per day the user can realistically dedicate to new habits",
    )
    current_streak_days: int = Field(
        default=0,
        description="How many days the user has been consistent with habits so far",
    )


class MicroHabitSuggestorTool(BaseTool):
    name: str = "Micro-Habit Suggestor"
    description: str = (
        "Suggests evidence-based micro-habits tailored to a specific wellness goal "
        "and the user's available time. Uses the 2-minute rule and habit stacking "
        "principles from behavioural psychology."
    )
    args_schema: Type[BaseModel] = MicroHabitInput

    HABIT_BANK: dict = {
        "stress": [
            ("2-min box breathing (4-4-4-4)", 2),
            ("5-min morning journaling — 3 things you control today", 5),
            ("Phone-free first 10 minutes after waking", 0),
            ("1-min body scan before each meal", 1),
            ("Evening: write 1 thing that went well", 2),
        ],
        "sleep": [
            ("No screens 20 min before bed — replace with reading", 0),
            ("Set a fixed wake time (even weekends)", 0),
            ("2-min progressive muscle relaxation at bedtime", 2),
            ("Cool room to 18–20°C before sleeping", 0),
            ("Morning sunlight exposure within 30 min of waking", 5),
        ],
        "weight": [
            ("Drink 500ml water before each meal", 1),
            ("Eat protein first at every meal", 0),
            ("10-min walk after dinner", 10),
            ("Log meals for 7 days (awareness, not restriction)", 5),
            ("Replace one processed snack with a whole food alternative", 0),
        ],
        "energy": [
            ("90-min focused work block, then 10-min movement break", 10),
            ("No caffeine after 2pm", 0),
            ("5-min midday stretching routine", 5),
            ("Consistent sleep/wake times (±30 min)", 0),
            ("Cold water face wash when energy dips", 1),
        ],
    }

    def _run(
        self, goal: str, available_minutes_per_day: int, current_streak_days: int = 0
    ) -> str:
        goal_lower = goal.lower()
        matched_key = next((k for k in self.HABIT_BANK if k in goal_lower), None)

        if not matched_key:
            habits = [h for habits in self.HABIT_BANK.values() for h in habits]
        else:
            habits = self.HABIT_BANK[matched_key]

        # Filter to habits that fit in available time
        fitting = [
            (name, mins) for name, mins in habits if mins <= available_minutes_per_day
        ]
        fitting = fitting[:4]  # Top 4

        level = (
            "Beginner"
            if current_streak_days < 7
            else "Intermediate"
            if current_streak_days < 30
            else "Advanced"
        )

        result = f"Micro-habits for '{goal}' | {available_minutes_per_day} min/day | Level: {level}\n\n"
        for i, (name, mins) in enumerate(fitting, 1):
            time_str = f"{mins} min" if mins > 0 else "0 min (mindset shift)"
            result += f"{i}. {name} — {time_str}\n"

        result += f"\nHabit stacking tip: Attach each habit to an existing anchor (e.g. after morning coffee, before bed)."
        return result


# ── Tool registry ─────────────────────────────────────────────────────────────


def get_nutrition_tools():
    return [BMICalculatorTool(), TDEECalculatorTool()]


def get_trainer_tools():
    return [BMICalculatorTool()]


def get_therapist_tools():
    return [MicroHabitSuggestorTool()]
