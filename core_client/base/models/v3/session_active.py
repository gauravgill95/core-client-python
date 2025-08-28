from pydantic import BaseModel
from typing import List, Optional

from . import SessionCollectorActiveSession


class SessionActive(BaseModel):
    """
    {
        "ffmpeg": [SessionCollectorActiveSession],
        "hls": [SessionCollectorActiveSession],
        "hlsingress": [SessionCollectorActiveSession],
        "http": [SessionCollectorActiveSession],
        "rtmp": [SessionCollectorActiveSession],
        "srt": [SessionCollectorActiveSession]
    }
    """

    ffmpeg: Optional[list[SessionCollectorActiveSession]]
    hls: Optional[list[SessionCollectorActiveSession]]
    hlsingress: Optional[list[SessionCollectorActiveSession]]
    http: Optional[list[SessionCollectorActiveSession]]
    rtmp: Optional[list[SessionCollectorActiveSession]]
    srt: Optional[list[SessionCollectorActiveSession]]
