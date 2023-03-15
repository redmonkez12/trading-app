from pydantic import BaseModel


class HealthcheckResponse(BaseModel):
    status: str
    last_update: str
