from pydantic import BaseModel
from typing import Dict, Optional

from . import ProcessConfigType, ProcessConfig, ProcessReport, ProcessState


class Process(BaseModel):
    """
    {
        "config": ProcessConfig,
        "created_at": "2022-07-27T12:00:49+00:00",
        "id": "restreamer-ui:ingest:c9e4b64b-5491-455f-b7ee-6b47d8842f74",
        "metadata": null,
        "reference": "c9e4b64b-5491-455f-b7ee-6b47d8842f74",
        "state": ProcessState,
        "report": ProcessReport,
        "type": ProcessConfigType
    }
    """

    config: Optional[ProcessConfig] = None
    created_at: Optional[int] = None
    id: Optional[str] = None
    metadata: Optional[Dict] = None
    reference: Optional[str] = None
    state: Optional[ProcessState] = None
    report: Optional[ProcessReport] = None
    type: Optional[ProcessConfigType] = None

    class Config:
        use_enum_values = True
