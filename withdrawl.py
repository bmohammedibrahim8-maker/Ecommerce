balance = 8000
while balance > 0:
    amount = int(input("Enter withdrawal amount:"))
    if amount <= balance:
         balance = balance-amount
         print("withdrawal successful")
         print("Remaining Balance = ",balance)
    else:
         print("Insufficient Balance")