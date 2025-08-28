from pydantic import BaseModel

from . import MetricsCollection


class MetricsCollectionList(BaseModel):
    data: list[MetricsCollection]