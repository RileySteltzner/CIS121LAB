def high_earnings(employee_salaries, threshold):
    results = []
    for name, salary in employee_salaries.items():
        if salary > threshold:
            results.append(name)
    return results
employee_salaries = {'Allice': 5000, 'Bob': 75000, 'Charlie': 10000}
print(high_earnings(employee_salaries, 6000 ))
    
