import csv
from collections import defaultdict

# Read the CSV and collect salaries by department
department_salaries = defaultdict(list)

with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        department = row['department']
        salary = float(row['salary'])
        department_salaries[department].append(salary)

# Calculate average salary per department
print('=' * 50)
print('       AVERAGE SALARY REPORT BY DEPARTMENT')
print('=' * 50)
print(f'{'Department':<20} {'Avg Salary':>15}')
print('-' * 50)

for dept in sorted(department_salaries.keys()):
    salaries = department_salaries[dept]
    avg_salary = sum(salaries) / len(salaries)
    print(f'{dept:<20} ${avg_salary:>14,.2f}')

print('-' * 50)
print(f'{'Total Employees':<20} {sum(len(s) for s in department_salaries.values()):>15}')
print('=' * 50)