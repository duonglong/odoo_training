import datetime
from typing import Optional

from pydantic import BaseModel


class StudentInfo(BaseModel):
    id: int
    name: Optional[str] = None
    date_of_birth: Optional[datetime.date] = None
    age: Optional[int] = None
    class_room: Optional[str] = None

    model_config = {"from_attributes": True}

class StudentCreateInfo(BaseModel):
    name: Optional[str] = None
    date_of_birth: Optional[datetime.date] = None
    age: Optional[int] = None
    class_room: Optional[str] = None

    model_config = {"from_attributes": True}
