from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogEntry:
    ip: str
    timestamp: datetime
    method: str
    path: str
    status: int
    bytes_sent: int