basic_pay = float(input("Enter the basic pay:"))
HRA = 0.10 * basic_pay
TA = 0.05 * basic_pay
total_salary = basic_pay + HRA + TA
print(f"Basic pay : {basic_pay}")
print(f"HRA (10%) : {HRA}")
print(f"TA (5%) : {TA}")
print(f"Total salary : {total_salary}")