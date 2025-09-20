import argparse
import csv
from collections import defaultdict
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser(description="Отчёт по успеваемости студентов")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список CSV файлов c данными об успеваемости"
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчёта (например, student-performance)"
    )
    return parser.parse_args()

def read_data(files):
    
    data = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data

def generate_student_performance(data):
    
    student_grades = defaultdict(list)

   
    for row in data:
        name = row["student_name"]
        grade = int(row["grade"])
        student_grades[name].append(grade)

    
    report = []
    for student, grades in student_grades.items():
        avg = sum(grades) / len(grades)
        report.append((student, round(avg, 2)))

   
    report.sort(key=lambda x: x[1], reverse=True)
    return report

def main():
    args = parse_args()
    data = read_data(args.files)

    if args.report == "student-performance":
        report = generate_student_performance(data)
        print(f"\nReport: {args.report}\n")
        print(tabulate(report, headers=["Student Name", "Average Grade"], tablefmt="github"))
    else:
        print(f"Отчёт {args.report} не поддерживается.")

if __name__ == "__main__":
    main()
