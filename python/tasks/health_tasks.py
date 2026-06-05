"""
WellnessMate Task Definitions + UserProfile dataclass.
Tasks pass context downstream: fitness sees nutrition output, wellness sees both.
"""
from crewai import Task, Agent
from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    age: int
    gender: str
    weight_kg: float
    height_cm: float
    activity_level: str       # sedentary | light | moderate | active | very_active
    primary_goal: str         # weight_loss | muscle_gain | general_fitness | stress_relief
    current_diet: str
    health_complaints: str
    available_equipment: str
    time_per_week_hours: int
    stress_level: int         # 1–10
    sleep_hours: float


def build_nutrition_task(profile: UserProfile, nutritionist: Agent) -> Task:
    return Task(
        description=(
            f"Create a personalised nutrition plan for the following user.\n\n"
            f"USER PROFILE\n"
            f"Name: {profile.name} | Age: {profile.age} | Gender: {profile.gender}\n"
            f"Weight: {profile.weight_kg} kg | Height: {profile.height_cm} cm\n"
            f"Activity level: {profile.activity_level} | Goal: {profile.primary_goal}\n"
            f"Current diet: {profile.current_diet}\n"
            f"Health complaints: {profile.health_complaints}\n\n"
            f"INSTRUCTIONS\n"
            f"1. Use BMI Calculator tool — assess weight status.\n"
            f"2. Use TDEE Calculator tool — establish daily calorie target.\n"
            f"3. Set macro targets (protein/carbs/fat in grams) for the goal.\n"
            f"4. Identify 3 nutritional gaps in the current diet.\n"
            f"5. Provide a sample 3-day meal plan (breakfast, lunch, dinner, snack).\n"
            f"   Use Indian/South Asian foods where relevant.\n"
            f"6. List 5 practical food swaps tailored to the current diet.\n"
            f"7. Note nutrition factors relevant to stated health complaints."
        ),
        expected_output=(
            "Nutrition report: BMI + TDEE values, daily macro targets, "
            "3 dietary gaps, 3-day meal plan, 5 food swaps, "
            "nutrition-complaint linkage note."
        ),
        agent=nutritionist,
    )


def build_fitness_task(
    profile: UserProfile, trainer: Agent, nutrition_task: Task
) -> Task:
    return Task(
        description=(
            f"Design a personalised workout programme for the following user.\n\n"
            f"USER PROFILE\n"
            f"Name: {profile.name} | Age: {profile.age} | Gender: {profile.gender}\n"
            f"Weight: {profile.weight_kg} kg | Height: {profile.height_cm} cm\n"
            f"Activity level: {profile.activity_level} | Goal: {profile.primary_goal}\n"
            f"Equipment: {profile.available_equipment}\n"
            f"Time available: {profile.time_per_week_hours} hours/week\n"
            f"Health complaints: {profile.health_complaints}\n\n"
            f"INSTRUCTIONS\n"
            f"1. Use BMI Calculator tool — confirm starting point.\n"
            f"2. Design a weekly training split within the time budget.\n"
            f"3. For each session: exercises, sets, reps, rest periods.\n"
            f"4. Include 1 mobility/flexibility routine targeting pain complaints.\n"
            f"5. Define a 4-week progressive overload plan.\n"
            f"6. List 3 exercises to AVOID given health complaints.\n"
            f"7. Align training intensity with calorie targets from the nutrition plan."
        ),
        expected_output=(
            "Fitness plan: weekly training split, session prescriptions "
            "(exercises/sets/reps/rest), mobility routine, 4-week progression, "
            "contraindicated movements, calorie-intensity alignment note."
        ),
        agent=trainer,
        context=[nutrition_task],
    )


def build_wellness_task(
    profile: UserProfile,
    therapist: Agent,
    nutrition_task: Task,
    fitness_task: Task,
) -> Task:
    return Task(
        description=(
            f"Conduct a mental wellness assessment and deliver a micro-habit plan.\n\n"
            f"USER PROFILE\n"
            f"Name: {profile.name} | Age: {profile.age}\n"
            f"Stress level: {profile.stress_level}/10\n"
            f"Average sleep: {profile.sleep_hours} hours/night\n"
            f"Primary goal: {profile.primary_goal}\n"
            f"Health complaints: {profile.health_complaints}\n\n"
            f"INSTRUCTIONS\n"
            f"1. Assess sleep quality from hours + complaints.\n"
            f"2. Identify the top 2 stress drivers in the profile.\n"
            f"3. Use the Micro-Habit Suggestor tool — goal = primary_goal, "
            f"   available_minutes_per_day = 10.\n"
            f"4. Prescribe a morning routine (max 10 min, 3–4 steps).\n"
            f"5. Prescribe an evening wind-down routine (max 15 min, 3–4 steps).\n"
            f"6. Recommend 1 breathing/mindfulness technique with exact instructions.\n"
            f"7. Note how the wellness plan supports nutrition and fitness recovery."
        ),
        expected_output=(
            "Wellness report: sleep assessment, top 2 stress drivers, "
            "4 micro-habits (Tiny Habits format), 10-min morning routine, "
            "15-min evening routine, 1 breathing technique with instructions, "
            "cross-plan integration note."
        ),
        agent=therapist,
        context=[nutrition_task, fitness_task],
    )
