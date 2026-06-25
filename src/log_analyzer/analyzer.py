from collections import Counter
from dataclasses import dataclass

from log_analyzer.models import LogEntry


@dataclass
class AnalysisResult:
    top_ips: list[tuple[str,int]]
    status_counts: dict[int, int]
    top_paths: list[tuple[str, int]]
    total_requests: int

def analyze(entries: list[LogEntry], top_n: int) -> AnalysisResult:
    ip_counter = Counter(entry.ip for entry in entries)
    path_counter = Counter(entry.path for entry in entries)
    total_requests = len(entries)
    status_counter = Counter(entry.status for entry in entries)
    statuses: dict[int, int] = dict(status_counter)
    result = AnalysisResult(
        top_ips= ip_counter.most_common(top_n),
        status_counts= statuses,
        top_paths= path_counter.most_common(top_n),
        total_requests= total_requests
    )
    return result


