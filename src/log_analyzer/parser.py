import datetime as dt
import re

from log_analyzer.models import LogEntry

from log_analyzer.exceptions import LogParseException

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<bytes>\S+)'
)

def parse_line(line: str) -> LogEntry:
    temp= LOG_PATTERN.match(line)
    if temp is None:
        raise LogParseException(line)
    log= temp.groupdict()
    try:
       time_stamp= dt.datetime.strptime(log['timestamp'], "%d/%b/%Y:%H:%M:%S %z")
    except ValueError as e:
        raise LogParseException(f'Неверная форма даты в {line}') from e
    log_entry= LogEntry(
        ip= log['ip'],
        timestamp= time_stamp,
        method= log['method'],
        path= log['path'],
        status= int(log['status']),
        bytes_sent= int(log['bytes']) if log['bytes'] != '-' else 0
    )

    return log_entry