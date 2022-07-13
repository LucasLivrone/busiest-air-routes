from pydantic import BaseModel


class Routes(BaseModel):
    route: str
    flights: int

    class Config:
        orm_mode = True
