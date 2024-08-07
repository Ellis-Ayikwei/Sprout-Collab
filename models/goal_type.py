#!/usr/bin/python3
"""the module for the collaborations"""
from models.basemodel import BaseModel, Base
import uuid
import sqlalchemy
from sqlalchemy import (
    Column,
    String
    
)



class Goal_type(BaseModel, Base):
    """Class definition for the goal_types"""
    __tablename__ = 'goal_types'
    name  = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    image_url = Column(String(500), nullable=True)
    

    def __init__(self, *args, **kwargs):
        """Initialization of the goal_types"""
        super().__init__(*args, **kwargs)