"""
Symptom Checker Module for WellnessMate
Provides basic health information and first aid guidance
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from loguru import logger
import json
import os

@dataclass
class SymptomInfo:
    """Data class for symptom information"""
    name: str
    description: str
    common_causes: List[str]
    self_care_tips: List[str]
    when_to_see_doctor: List[str]
    severity: str  # 'mild', 'moderate', 'severe'
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'common_causes': self.common_causes,
            'self_care_tips': self.self_care_tips,
            'when_to_see_doctor': self.when_to_see_doctor,
            'severity': self.severity
        }

class SymptomChecker:
    """Symptom checker for providing health information"""
    
    def __init__(self, knowledge_base_path: Optional[str] = None):
        """
        Initialize the symptom checker
        
        Args:
            knowledge_base_path: Path to a JSON file with symptom information
        """
        self.knowledge_base: Dict[str, SymptomInfo] = {}
        self.initialized = False
        self.knowledge_base_path = knowledge_base_path or os.path.join(
            os.path.dirname(__file__), 'data', 'symptoms_kb.json'
        )
    
    async def initialize(self):
        """Load the symptom knowledge base"""
        if self.initialized:
            return
            
        logger.info("Initializing Symptom Checker...")
        
        # In a real implementation, we would load from a knowledge base
        # For now, we'll use a small in-memory database
        self.knowledge_base = {
            'headache': SymptomInfo(
                name="Headache",
                description="Pain or discomfort in the head or face area.",
                common_causes=[
                    "Tension or stress",
                    "Dehydration",
                    "Lack of sleep",
                    "Eye strain",
                    "Sinus congestion"
                ],
                self_care_tips=[
                    "Drink water to stay hydrated",
                    "Rest in a quiet, dark room",
                    "Apply a cold or warm compress to your head or neck",
                    "Practice relaxation techniques"
                ],
                when_to_see_doctor=[
                    "Headache is severe and sudden",
                    "Accompanied by fever, stiff neck, or confusion",
                    "Follows a head injury",
                    "Worsens over time"
                ],
                severity="moderate"
            ),
            # Add more symptoms as needed
        }
        
        self.initialized = True
        logger.info(f"Symptom Checker initialized with {len(self.knowledge_base)} symptoms")
    
    async def check_symptom(self, symptom_name: str) -> Optional[Dict]:
        """
        Get information about a specific symptom
        
        Args:
            symptom_name: Name of the symptom to look up
            
        Returns:
            Dict with symptom information, or None if not found
        """
        if not self.initialized:
            await self.initialize()
            
        # Simple case-insensitive search
        symptom_name = symptom_name.lower().strip()
        
        # Try exact match first
        if symptom_name in self.knowledge_base:
            return self.knowledge_base[symptom_name].to_dict()
            
        # Try partial match
        for key, symptom in self.knowledge_base.items():
            if symptom_name in key or key in symptom_name:
                return symptom.to_dict()
                
        return None
    
    async def search_symptoms(self, query: str) -> List[Dict]:
        """
        Search for symptoms matching a query
        
        Args:
            query: Search query
            
        Returns:
            List of matching symptoms
        """
        if not self.initialized:
            await self.initialize()
            
        query = query.lower().strip()
        results = []
        
        for name, symptom in self.knowledge_base.items():
            if query in name or query in symptom.description.lower():
                results.append(symptom.to_dict())
                
        return results

# Singleton instance
symptom_checker = SymptomChecker()

async def get_symptom_checker() -> SymptomChecker:
    """Get the shared SymptomChecker instance"""
    return symptom_checker
