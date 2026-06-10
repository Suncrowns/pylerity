from pylerity.user import User
from pylerity.groups import Group


class GroupFilterFields:
    post_fields = ["active", "color", "description", "maxDevices", "name", "subscriptionTitle"]


class UserFilterFields:
    post_fields = ["userId", "enabled", "expireAt", "groups", "trafficLimit", "username"]
    put_fields = ["userId", "enabled", "expireAt", "groups", "hwidEnforceFrom", "hwidMode", "maxDevices", "trafficLimit", "username"]



def validate_user(user: User):
    if user.hwidMode not in [None, "inherit", "off", "strict"]:
        return False 
    return user



def filter_data(data: dict, fields: list):
    return {k: v for k, v in data.items() if k in fields}
        