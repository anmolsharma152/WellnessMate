"""
WellnessMate CLI
  python -m python.main          # interactive
  python -m python.main --demo   # demo profile
"""

import argparse, os, sys

import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from dotenv import load_dotenv

load_dotenv()


def demo_profile():
    from .tasks.health_tasks import UserProfile

    return UserProfile(
        name="Demo User",
        age=28,
        gender="male",
        weight_kg=78.0,
        height_cm=175.0,
        activity_level="light",
        primary_goal="weight_loss",
        current_diet="North Indian home food — dal/roti/sabzi, skips breakfast, heavy dinner at 10pm, 3 cups chai",
        health_complaints="lower back pain (8hrs desk), afternoon energy crash, poor sleep",
        available_equipment="10kg dumbbells + yoga mat",
        time_per_week_hours=4,
        stress_level=7,
        sleep_hours=6.0,
    )


def interactive_profile():
    from .tasks.health_tasks import UserProfile

    print("\n" + "=" * 60)
    print("  WellnessMate — Personal Wellness Assessment")
    print("=" * 60 + "\n")

    def ask(prompt, default, cast=str):
        raw = input(f"{prompt} [{default}]: ").strip()
        return cast(raw) if raw else cast(default)

    name = ask("Name", "User")
    age = ask("Age", 25, int)
    gender = ask("Gender (male/female)", "male")
    weight = ask("Weight kg", 70, float)
    height = ask("Height cm", 170, float)
    print("\n  sedentary | light | moderate | active | very_active")
    activity = ask("Activity level", "moderate")
    print("  weight_loss | muscle_gain | general_fitness | stress_relief")
    goal = ask("Primary goal", "general_fitness")
    diet = ask("Current diet", "mixed, 3 meals/day")
    complaints = ask("Health complaints", "none")
    equipment = ask("Equipment", "bodyweight only")
    time_hrs = ask("Exercise hours/week", 4, int)
    stress = ask("Stress 1–10", 5, int)
    sleep = ask("Sleep hours/night", 7.0, float)
    return UserProfile(
        name=name,
        age=age,
        gender=gender,
        weight_kg=weight,
        height_cm=height,
        activity_level=activity,
        primary_goal=goal,
        current_diet=diet,
        health_complaints=complaints,
        available_equipment=equipment,
        time_per_week_hours=time_hrs,
        stress_level=stress,
        sleep_hours=sleep,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY not set. Add to .env file.")
        sys.exit(1)
    from .crew import run_wellness_assessment

    profile = demo_profile() if args.demo else interactive_profile()
    print(f"\n🚀 Running assessment for {profile.name}...\n")
    report = run_wellness_assessment(profile)
    print(f"\n{'=' * 60}\n  WELLNESS PLAN\n{'=' * 60}\n{report}")
    fname = f"wellness_plan_{profile.name.lower().replace(' ', '_')}.txt"
    with open(fname, "w") as f:
        f.write(report)
    print(f"\n✅ Saved to {fname}")


if __name__ == "__main__":
    main()
