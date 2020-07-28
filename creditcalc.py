import argparse
import math


def error_message():
    print('Incorrect parameters')


def count_annuity_payment(credit_principal, months, monthly_interest):
    monthly_interest = monthly_interest / 12 / 100
    x = pow(1 + monthly_interest, months)  # for shorten purpose
    monthly_payment = credit_principal * monthly_interest * x / (x - 1)
    if (math.modf(monthly_payment))[0] == 0:
        print(f'Your annuity payment = {int(monthly_payment)}!')
        print(f'Overpayment = {int(monthly_payment) * months - credit_principal}')
    else:
        print(f'Your annuity payment = {int(monthly_payment) + 1}!')
        print(f'Overpayment = {int(monthly_payment + 1) * months - credit_principal}')


def count_principal(monthly_payment, months, monthly_interest):
    monthly_interest = monthly_interest / 12 / 100
    x = pow(1 + monthly_interest, months)  # for shorten purpose
    credit_principal = monthly_payment / (monthly_interest * x) * (x - 1)
    print(f'Your credit principal = {int(credit_principal)}!')
    print(f'Overpayment = {monthly_payment * months - int(credit_principal)}')


def count_months(credit_principal, monthly_payment, monthly_interest):
    monthly_interest = monthly_interest / 12 / 100
    months = math.log(monthly_payment / (monthly_payment - monthly_interest * credit_principal), 1 + monthly_interest)
    if (math.modf(months))[0] != 0:
        months = (math.modf(months))[1] + 1
    overpayment = monthly_payment * int(months) - credit_principal
    year = months // 12
    months = months % 12
    if year == 0 and months != 1:  # plural months
        print(f'You need {int(months)} months to repay this credit!')
        print(f'Overpayment = {overpayment}')
    elif year == 1 and months == 0:  # single year
        print(f'You need {int(year)} year to repay this credit!')
        print(f'Overpayment = {overpayment}')
    elif months == 1 and year == 0:
        print(f'You need {int(months)} month to repay this credit!')
        print(f'Overpayment = {overpayment}')
    elif year != 1 and months == 0:
        print(f'You need {int(year)} years to repay this credit!')
        print(f'Overpayment = {overpayment}')
    else:
        print(f'You need {int(year)} years and {int(months)} months to repay this credit!')
        print(f'Overpayment = {overpayment}')


def count_diff_payment(credit_principal, months, monthly_interest):
    monthly_interest = monthly_interest / 12 / 100
    paid = 0
    for x in range(1, months + 1):
        part = credit_principal - credit_principal * (x - 1) / months
        payment = credit_principal / months + monthly_interest * part
        if (math.modf(payment))[0] == 0:
            print(f'Month {x}: paid out {int(payment)}')
            paid = paid + int(payment)
        else:
            print(f'Month {x}: paid out {int(payment) + 1}')
            paid = paid + int(payment) + 1
    print()
    print(f'Overpayment = {paid - credit_principal}')


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
# below are conditions that cause error
if not args.type or (args.type != 'annuity' and args.type != 'diff'):
    error_message()
elif args.type == 'diff' and args.payment:
    error_message()
elif not args.interest:
    error_message()
# below are the calculations
elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    count_annuity_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    count_principal(args.payment, args.periods, args.interest)
elif args.type == 'annuity' and args.principal and args.payment and args.interest:
    count_months(args.principal, args.payment, args.interest)
elif args.type == 'diff' and args.principal and args.periods and args.interest:
    count_diff_payment(args.principal, args.periods, args.interest)
else:
    error_message()
