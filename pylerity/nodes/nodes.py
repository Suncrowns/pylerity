from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Any
from enum import Enum
from pylerity.groups import Group


class CascadeRole(Enum):
    standalone = "standalone",
    portal = "portal"
    bridge = "bridge"


class NodeType(Enum):
    hysteria = "hysteria"
    xray = "xray"
    virtual = "virtual"


class SSH(BaseModel):
    password: str
    port: int
    privateKey: str
    username: str


class Node(BaseModel):
    """POST section"""
    name: str 
    cascadeRole: str | CascadeRole
    comment: str = Field(max_length=500)
    country: str 
    domain: str 
    groups: List[Group]
    ip: str 
    maxOnlineUsers: int | None = Field(default=0)
    port: int 
    portRange: str 
    rankingCoefficient: int | None = Field(default=0)
    sni: str | None = Field(default=None)

    ssh: SSH | None = Field(default=None)
    type: NodeType | str


    """GET section"""