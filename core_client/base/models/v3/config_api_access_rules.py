from pydantic import BaseModel
from typing import Optional, List


class ConfigApiAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[list[str]]
    block: Optional[list[str]]
