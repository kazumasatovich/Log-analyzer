import argparse
from pathlib import Path

from analyzer import analyze
from exceptions import LogParseException
from models import LogEntry
from parser import parse_line
from report import format_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="log-analyzer",
        description="Анализатор access-логов сервера (Apache/Nginx combined)"
    )
    parser.add_argument("log_file", type=Path, help="Путь к лог-файлу")
    parser.add_argument(
        "--top", type=int, default=10, help="Сколько топовых записей показать?"
    )
    parser.add_argument("--format",
                        choices=["text", "json"],
                        default= "text",
                        help="Формат вывода отчета",
    )
    parser.add_argument("--output", type=Path, default= None,
                         help="Файл для сохранения отчета")
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.log_file.exists():
        parser.error(f"Файл не найден: {args.log_file}")

    print(f"Анализ файла {args.log_file}, top={args.top}, format={args.format}\n")
    failed_counts = 0
    entries: list[LogEntry] = []
    lines_count = 0
    skipped_count = 0
    with open(args.log_file, encoding= "utf-8") as f:
        for raw_line in f:
            lines_count += 1
            line = raw_line.strip()
            if not line:
                skipped_count += 1
                continue
            try:
                entry = parse_line(line)
                entries.append(entry)
            except LogParseException:
                failed_counts += 1
    print(f'Прочитанных строк: {lines_count}\n'
          f'Успешно считано: {lines_count - skipped_count - failed_counts} строк\n'
          f'Не удалось прочитать: {failed_counts} строк\n'
          f'Пропущено: {skipped_count} пустых строк'
          f'\n')
    result = analyze(entries, args.top)
    report_text = format_report(result, args.format)
    if args.output is not None:
        args.output.write_text(report_text, encoding="utf-8")
        print(f"Отчёт сохранен в {args.output}")
    else:
        print(report_text)
if __name__ == "__main__":
    main()
