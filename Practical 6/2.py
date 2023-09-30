def get_salary_details(basic_salary):
    DA = basic_salary * 0.7
    MA = 100
    TA = 400
    TOTAL_SALARY = basic_salary + DA + MA + TA
    return DA, MA, TA, TOTAL_SALARY

basic_salary = float(input("Enter basic salary: "))
DA, MA, TA, total_salary = get_salary_details(basic_salary)
print("DA:", DA, "MA:", MA, "TA:", TA, "TOTAL_SALARY:", total_salary)
