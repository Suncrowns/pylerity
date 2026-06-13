from pydantic import Field, BaseModel, ConfigDict


class Group(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )
    name: str 

    """GET section"""
    id: str | None = Field(default=None, validation_alias="_id", serialization_alias="_id") 

    """POST/PUT section"""
    active: bool | None = Field(default=None)
    color: str | None = Field(default=None)
    description: str | None = Field(default=None)
    maxDevices: int | None = Field(default=None)
    subscriptionTitle: str | None = Field(default=None)
