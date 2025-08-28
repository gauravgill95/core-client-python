from pydantic import BaseModel
from typing import Union, List


class SkillsCodecsType(BaseModel):
    """
    {
        "decoders": [
            "string"
        ],
        "encoders": [
            "string"
        ],
        "id": "string",
        "name": "string"
    }
    """

    decoders: Union[None, list[str]]
    encoders: Union[None, list[str]]
    id: str
    name: str
