from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt


class DonationBase(BaseModel):
    full_amount: PositiveInt = Field()
    comment: Optional[str] = Field()

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class DonationView(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationView):
    user_id: Optional[int]
    invested_amount: NonNegativeInt = Field(0)
    fully_invested: bool = Field(False)
    close_date: Optional[datetime]
