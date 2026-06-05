"""WellnessMate Crew — Orchestration"""

import os
from typing import Optional
from crewai import Crew, Process, LLM
from dotenv import load_dotenv

from .agents import create_nutritionist, create_trainer, create_therapist
from .tasks.health_tasks import (
    UserProfile,
    build_nutrition_task,
    build_fitness_task,
    build_wellness_task,
)

load_dotenv()


def build_crew(profile: UserProfile, groq_api_key: Optional[str] = None) -> Crew:
    api_key = groq_api_key or os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set. Add to .env:\n  GROQ_API_KEY=gsk_...")

    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        max_retries=5,
        api_key=api_key,
        temperature=0.7,
        max_tokens=2048,
    )

    nutritionist = create_nutritionist(llm)
    trainer = create_trainer(llm)
    therapist = create_therapist(llm)

    nutrition_task = build_nutrition_task(profile, nutritionist)
    fitness_task = build_fitness_task(profile, trainer, nutrition_task)
    wellness_task = build_wellness_task(
        profile, therapist, nutrition_task, fitness_task
    )

    return Crew(
        agents=[nutritionist, trainer, therapist],
        tasks=[nutrition_task, fitness_task, wellness_task],
        process=Process.sequential,
        max_rpm=2,
        verbose=True,
    )


def run_wellness_assessment(profile: UserProfile) -> str:
    return str(build_crew(profile).kickoff())
