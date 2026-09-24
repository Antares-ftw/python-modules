from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0, le=100)
    oxygen_level: float = Field(..., ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    s = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational=True,
        last_maintenance=datetime.now(),
    )
    print(
        "Space Station Data Validation\n"
        + "========================================\n"
        + f"ID: {s.station_id}\n"
        + f"Name: {s.name}\n"
        + f"Crew: {s.crew_size} people\n"
        + f"Power: {s.power_level}%\n"
        + f"Oxygen: {s.oxygen_level}%\n"
        + f"Status: {'Operational'
                     if s.is_operational
                     else 'Not Operational'}\n"
        + "\n========================================\n"
        + "Expected validation error:"
    )
    try:
        s = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=9001,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        error_str = str(e).split("\n")[2][2:42]
        print(error_str)
