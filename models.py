from pydantic import BaseModel
from typing import List, Dict, Optional, Any

class Parameter(BaseModel):
    name: str
    value: Optional[Any] = None
    unit: Optional[str] = None

class OrderablePartDetails(BaseModel):
    description: str
    parameters: List[Parameter]

class DescriptionTableItem(BaseModel):
    part_number: str
    description: Optional[str] = None
    important_info: Optional[str] = None

class PartData(BaseModel):
    company_name: str
    generic_part_number: str
    orderable_part_numbers: Dict[str, OrderablePartDetails]
    description_table: List[DescriptionTableItem]

