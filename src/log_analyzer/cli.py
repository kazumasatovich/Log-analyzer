import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="log-analyzer",
        description="Анализатор acces-логов сервера (ApacheNginx combined)"
    )
    parser.add_argument("log_file", type=Path, help="Путь к лог-файлу")
    parser.add_argument(
        "--top", type=int, default=10, help="Сколько топовых записей показать?"
    )
    parser.add_argument("--format",
                        choices=["txt", "json"],
                        default= "txt",
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

    print(f"Анализ файла {args.log_file}, top={args.top}, format={args.format}")

if __name__ == "__main__":
    main()
