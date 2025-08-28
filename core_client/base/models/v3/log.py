from pydantic import BaseModel
from typing import List, Union


class Log(BaseModel):
    data: List[Union[str, dict]]