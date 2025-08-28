from pydantic import BaseModel
from typing import Optional, List


class ConfigFfmpegAccessRules(BaseModel):
    """
    {
        "allow": [],
        "block": []
    }
    """

    allow: Optional[list[str]]
    block: Optional[list[str]]
