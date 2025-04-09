
from typing import Dict, Any, List
from refiner.models.refined import Base
from refiner.transformer.base_transformer import DataTransformer
from refiner.models.refined import DataRefined
from refiner.models.unrefined import UnrefinedData

class UserTransformer(DataTransformer):
    """
    Transformer for user data as defined in the example.
    """
    
    def transform(self, data: Dict[str, Any]) -> List[Base]:
        """
        Transform raw user data into SQLAlchemy model instances.
        
        Args:
            data: Dictionary containing user data
            
        Returns:
            List of SQLAlchemy model instances
        """
        # Validate data with Pydantic
        unrefined_data = UnrefinedData.model_validate(data)
        
        # Create data instance
        refined_data = DataRefined(
            date=unrefined_data.date,
            files=unrefined_data.files,
            owner=unrefined_data.owner
        )
        
        return [refined_data]
