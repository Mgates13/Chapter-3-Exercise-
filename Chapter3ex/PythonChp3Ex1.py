##########
#Morgan-Python Chapter 3
#Exercise 1
#Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for worked above 40hours
##########

hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
OVERTIME_RATE = 1.5


def pay(hours, rate):
    ''' Determine pay given hours and rate and 1.5 times the hourly
    rate for hours worked above 40.'''
    overtime_pay = 0
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * OVERTIME_RATE
        final_pay = ((hours - overtime_hours) * rate) + overtime_pay
    else:
        final_pay = (hours * rate)
    return "Pay: " + str(final_pay)

print pay(hours, rate)
