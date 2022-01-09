# Import external dependencies
from sqlalchemy import Column, Integer, Float
from typing import Optional

# Import local dependency
from db import Base

# Define class
class Experience(Base):

    __tablename__ = "experiences"
    __table_args__ = {'sqlite_autoincrement': True}

    # Mandatory fields 
    id = Column(Integer,primary_key=True, index=True, nullable=False)
    Machine_N_cycles = Column(Integer)
    Machine_Load = Column(Float)
    Machine_Displacement = Column(Float)

    # Optional fields, set by default to None
    
    # index: Optional[Column(Integer)] = None
    # Camera_N_cycles: Optional[Column(Float)] = None
    # exx: Optional[Column(Float)] = None
    # eyy: Optional[Column(Float)] = None
    # exy: Optional[Column(Float)] = None
    # crack_length: Optional[Column(Float)] = None
    # Th_time: Optional[Column(Time)] = None
    # Th_N_cycles: Optional[Column(Float)] = None
    # Th_specimen_max: Optional[Column(Float)] = None
    # Th_specimen_mean: Optional[Column(Float)] = None
    # Th_chamber: Optional[Column(Float)] = None
    # Th_uppergrips: Optional[Column(Float)] = None
    # Th_lowergrips: Optional[Column(Float)] = None
    