# and
# or
# not

high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Eligable")

if high_income or good_credit:
    print("Eligable")

if not student:
    print("Eligible")

if (high_income or good_credit) and not student:
    print("Eligable")
