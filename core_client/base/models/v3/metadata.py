from pydantic import BaseModel
from typing import Union


class Metadata(BaseModel):
    data: Union[int, float, str, dict, list]