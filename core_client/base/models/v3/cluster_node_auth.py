from pydantic import BaseModel, AnyUrl


class ClusterNodeAuth(BaseModel):
    address: AnyUrl
    username: str
    password: str
