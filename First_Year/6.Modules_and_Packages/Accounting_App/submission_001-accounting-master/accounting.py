import sys
from user.authentication import authenticate_user
from transactions.journal import receive_income, pay_expense
from banking.fvb.reconciliation import do_reconciliation


if len(sys.argv) > 1:
    for arg in sys.argv[1::]:
        print(arg)


if __name__ == "__main__":
    authenticate_user()
    amount = 100 
    receive_income(amount)
    pay_expense(amount)
    do_reconciliation()
    

