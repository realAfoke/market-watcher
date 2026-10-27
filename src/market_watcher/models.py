from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Observation:
    source:str
    item:str
    value:int
    observed_at:datetime

