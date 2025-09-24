# Student Performance Report Generator

Программа для генерации отчётов об успеваемости студентов из CSV-файлов.

## Установка

```bash
git clone https://github.com/hyd3-me/python_jun_test_24.09.git source
python -m venv env
source /env/bin/activate
cd source
pip install -r requirements.txt
```

## Запуск
```
python src/main.py --files students1.csv students2.csv --report student-performance
```

## Структура проекта
```
source/
├── src/
│   ├── cli.py                 # Обработка аргументов
│   ├── main.py                # Точка входа
│   ├── parsers/
│   │   └── csv_parser.py      # Чтение CSV
│   └── reports/
│       ├── base.py            # Абстрактный класс отчёта
│       ├── manager.py         # Менеджер отчётов
│       └── student_performance.py  # Отчёт по успеваемости
├── tests/
│   ├── test_cli.py
│   ├── test_csv_parser.py
│   ├── test_main.py
│   └── test_reports/
│       ├── test_base.py
│       ├── test_manager.py
│       └── test_student_performance.py
├── requirements.txt
└── README.md
```

## Как добавить новый отчет
```
- Создайте класс, наследующийся от BaseReport.
- Реализуйте метод generate.
- Зарегистрируйте отчёт в ReportManager.
```

### Пример:
```
from reports.base import BaseReport

class NewReport(BaseReport):
    def generate(self, data):
        return "..."
```

## Тесты
```
python -m pytest tests/
```

### Покрытие тестами

![test cov](image-7.png)


## Примеры запуска скрипта:

### запуск для одного файла
![with 1 file](image.png)

### запуск для двух файлов
![with 2 files](image-2.png)

### запуск с неправильным именем отчета
![wrong_report_name](image-3.png)

### запуск без флага отчета
![without --report](image-4.png)

### запуск без указания пути к файлу
![empty file list](image-5.png)

### запуск без указания флага файлов
![no --files arg](image-6.png)