from pydantic import (
        BaseModel,
        Field,
        model_validator,
        ValidationError
        )
from typing import Optional, Annotated
from typing_extensions import Self
from datetime import datetime
from enum import Enum, auto


class ContactType(Enum):
    radio = auto()
    visual = auto()
    physical = auto()
    telepathic = auto()

    @classmethod
    def deenum(cls, value: Self) -> str:
        if value == cls.radio:
            return "radio"
        elif value == cls.visual:
            return "visual"
        elif value == cls.physical:
            return "physical"
        else:
            return "telepathic"


class AlienContact(BaseModel):
    contact_id: Annotated[
        str,
        Field(
            ...,
            description="String, 5-15 characters",
            min_length=5,
            max_length=15
            ),
    ]
    timestamp: datetime = Field(..., description="DateTime of contact")
    contact_type: ContactType = Field(..., description="ContactType enum")
    signal_strength: Annotated[
        float, Field(
            ...,
            description="signal strength 0-10.0",
            ge=0.0,
            le=10.0
            )
    ]
    location: Annotated[
        str, Field(..., description="location", min_length=3, max_length=100)
    ]
    duration_minutes: Annotated[
        int, Field(
            ...,
            description="Duration of contact (max 24 hours)",
            ge=1,
            le=1440
            )
    ]
    witness_count: Annotated[
            int,
            Field(
                ...,
                description="witness count",
                ge=1,
                le=100
                )
            ]
    message_received: Optional[
        Annotated[str, Field(description="message received", max_length=500)]
    ]
    is_verified: Annotated[
            bool,
            Field(description="Is the contact verified?")] = False

    @model_validator(mode="after")
    def extended_requirements(self) -> Self:
        if self.contact_id[:2] != "AC":
            raise ValueError("id mast start with 'AC'")
        elif (
                self.contact_type == ContactType.physical
                and
                not self.is_verified
                ):
            raise ValueError("Physical contact reports must be verified")
        elif (
                self.contact_type == ContactType.telepathic
                and
                self.witness_count < 3
                ):
            raise ValueError(
                    "Telepathic contact requires "
                    + "at least 3 witnesses"
                    )
        elif self.witness_count > 7 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include " + "received messages"
            )
        return self


if __name__ == "__main__":
    cont = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        contact_type=ContactType.radio,
        signal_strength=8.50,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        location="Area 51, Nevada",
    )
    print(
        "Alien Contact Log Validation\n"
        + "======================================\n"
        + "Valid contact report:\n"
        + f"ID: {cont.contact_id}\n"
        + f"Type: {ContactType.deenum(cont.contact_type)}\n"
        + f"Location: {cont.location}\n"
        + f"Signal: {cont.signal_strength}/10\n"
        + f"Duration: {cont.duration_minutes} minutes\n"
        + f"Witnesses: {cont.witness_count}"
        + f"{'\nMessage: \''+cont.message_received+'\''
             if cont.message_received is not None else ''}"
        + "\n\n======================================\n"
        + "Expected validation error:"
    )
    try:
        cont = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.telepathic,
            signal_strength=8.50,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            location="Area 51, Nevada",
        )
    except ValidationError as e:
        print("".join(str(e).split(",")[1].split("[")[0]))
