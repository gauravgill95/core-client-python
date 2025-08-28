from pydantic import BaseModel
from typing import List, Optional


class ConfigStorageDiskCacheTypes(BaseModel):
    """
    {
        "allow": [],
        "block": [".m3u8"]
    }
    """

    allow: Optional[list[str]]
    block: Optional[list[str]]
