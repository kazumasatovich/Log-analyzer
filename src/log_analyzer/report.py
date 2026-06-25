import json
from dataclasses import asdict

from log_analyzer.analyzer import AnalysisResult


def format_text(result: AnalysisResult) -> str:
    lines = [
        f"Всего запросов: {result.total_requests}"
        "\n"
        "\n"
        "Топ IP:"
    ]
    for c, (ip, count) in enumerate(result.top_ips, start=1):
        lines.append(f"{c} - {ip}: {count}")
    lines.append("")
    lines.append("Топ статусов:")
    for c, (status, count) in enumerate(sorted(result.status_counts.items()), start=1):
        lines.append(f"{c} - {status}: {count}")
    lines.append("")
    lines.append("Топ путей:")
    for c, (path, count) in enumerate(result.top_paths, start=1):
        lines.append(f"{c} - {path}: {count}")
    return "\n".join(lines)

def format_json(result: AnalysisResult) -> str:
    return json.dumps(asdict(result), indent=1, ensure_ascii=False)

def format_report(result: AnalysisResult, fmt: str) -> str:
    if fmt == "json":
        return format_json(result)
    return format_text(result)
