# Log Analyzer

CLI-инструмент для анализа access-логов сервера (Apache/Nginx combined format).
Считает топ IP по количеству запросов, статистику по статус-кодам, топ запрашиваемых путей.

## Запуск (в разработке)
python -m log_analyzer.cli <путь-к-логу> --top 10 --format text
