from pydantic import (
    BaseModel,
    Field,
    model_validator,
    ValidationError,
)
from typing_extensions import Self
from datetime import datetime
from enum import Enum, auto


class Rank(Enum):
    cadet = auto()
    officer = auto()
    lieutenant = auto()
    captain = auto()
    commander = auto()

    @classmethod
    def deenum(cls, enum: Self) -> str:
        if enum == cls.cadet:
            return "cadet"
        elif enum == cls.officer:
            return "officer"
        elif enum == cls.lieutenant:
            return "lieutenant"
        elif enum == cls.captain:
            return "captain"
        else:
            return "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

    @classmethod
    def print_guys(cls, crew: list[Self]) -> None:
        for guy in crew:
            print(
                    f"- {guy.name} ({Rank.deenum(guy.rank)}) "
                    + f"- {guy.specialization}"
                    )


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def extended_requirements(self) -> Self:
        if self.mission_id[:1] != "M":
            raise ValueError("id mast start with 'ac'")
        elif not any(
            [
                x.rank == Rank.commander
                or
                x.rank == Rank.captain
                for x in self.crew
                ]
        ):
            raise ValueError("Must have at least one Commander or Captain")
        return self


if __name__ == "__main__":
    crew_list = [
        CrewMember(
            member_id="GUY001",
            name="Sarah Connor",
            rank=Rank.commander,
            specialization="Mission Command",
            age=30,
            years_experience=10,
        ),
        CrewMember(
            member_id="GUY002",
            name="John Smith",
            rank=Rank.lieutenant,
            specialization="Navigation",
            age=30,
            years_experience=10,
        ),
        CrewMember(
            member_id="GUY003",
            name="Alice Johnson",
            rank=Rank.officer,
            specialization="Engineering",
            age=30,
            years_experience=10,
        ),
    ]
    mission = SpaceMission(
        mission_id="M12024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=crew_list,
        budget_millions=2500.0,
    )
    print(
        "Space Mission Crew Validation\n"
        + "=========================================\n"
        + "Valid mission created:\n"
        + f"Mission: {mission.mission_name}\n"
        + f"ID: {mission.mission_id}\n"
        + f"Destination: {mission.destination}\n"
        + f"Duration: {mission.duration_days} days\n"
        + f"Budget: ${mission.budget_millions}M\n"
        + f"Crew size: {len(mission.crew)}\n"
        + "Crew members:"
    )
    CrewMember.print_guys(mission.crew)
    print(
        "\n=========================================\n"
        + "Expected validation error:"
    )
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print(e)
    crew_list2 = [
        CrewMember(
            member_id="GUY001",
            name="Sarah Connor",
            rank=Rank.cadet,
            specialization="Mission Command",
            age=30,
            years_experience=10,
        ),
        CrewMember(
            member_id="GUY002",
            name="John Smith",
            rank=Rank.lieutenant,
            specialization="Navigation",
            age=30,
            years_experience=10,
        ),
        CrewMember(
            member_id="GUY003",
            name="Alice Johnson",
            rank=Rank.cadet,
            specialization="Engineering",
            age=30,
            years_experience=10,
        ),
    ]
    try:
        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew_list2,
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print("".join(str(e).split(",")[1].split("[")[0]))
