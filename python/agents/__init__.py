"""
AI Agents for WellnessMate

This package contains the various AI agents that power the WellnessMate application,
including nutritionists, trainers, and therapists.
"""

from typing import Dict, Any, Optional

class BaseAgent:
    """Base class for all AI agents"""
    
    def __init__(self, name: str, role: str, goal: str):
        """
        Initialize the base agent
        
        Args:
            name: The name of the agent
            role: The role of the agent (e.g., 'nutritionist', 'trainer', 'therapist')
            goal: The primary goal of the agent
        """
        self.name = name
        self.role = role
        self.goal = goal
        self.initialized = False
    
    async def initialize(self):
        """Initialize the agent's resources"""
        self.initialized = True
    
    async def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process a user query
        
        Args:
            query: The user's query
            context: Additional context for the query
            
        Returns:
            str: The agent's response
        """
        if not self.initialized:
            await self.initialize()
            
        return f"I am {self.name}, your {self.role}. I'm here to help with: {self.goal}"

# Import agent implementations here
# from .nutritionist import NutritionistAgent
# from .trainer import TrainerAgent
# from .therapist import TherapistAgent

__all__ = [
    'BaseAgent',
    # 'NutritionistAgent',
    # 'TrainerAgent',
    # 'TherapistAgent',
]
