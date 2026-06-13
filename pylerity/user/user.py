from pydantic import Field, BaseModel, ConfigDict
from datetime import datetime 


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )
    
    """POST section"""
    user_id: str = Field(validation_alias="userId", serialization_alias="userId")
    enabled: bool 
    expireAt: str | None = Field(default=None)
    groups: list | None = Field(default=[])
    trafficLimit: int | None = Field(default=0)
    username: str 

    """GET/PUT section"""
    id: str | None = Field(default = None, serialization_alias="_id")
    password: str | None = Field(default=None)
    xrayUuid: str | None = Field(default=None)
    nodes: list | None = Field(default=None)
    maxDevices: int | None = Field(default=None)
    hwidMode: str | None = Field(default=None)
    subscriptionToken: str | None = Field(default=None)
    traffic: dict | None = Field(default=None)
    createdAt: str | int | None = Field(default=None)
    updatedAt : str | int | None = Field(default=None)

