from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime


class Model(BaseModel):
    Company_name : str = Field(...)
    Agenda_of_meeting: str= Field(...)
    participants: list= Field(...,default=list)
    
    At_what_time : Optional[datetime]
    type_of_meeting:Optional[str]
    
    expected_duration:Optional[int] = Field(default=None)   # This should be integer of minutes how many minutes
    
    location:Optional[str]



