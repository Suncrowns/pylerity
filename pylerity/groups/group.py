from pydantic import Field, BaseModel 


class Group(BaseModel):
    name: str 

    """GET section"""
    id: str | None = Field(default=None, alias="_id", serialization_alias="_id") 

    """POST/PUT section"""
    active: bool | None = Field(default=None)
    color: str | None = Field(default=None)
    description: str | None = Field(default=None)
    maxDevices: int | None = Field(default=None)
    subscriptionTitle: str | None = Field(default=None)
