accounts = {"Jade": 1000,
            "Shayne": 10000,
            "Jason": 200000,
            "Rotherford": 1000000,
            "Edward": 500000,
            "Paul": 300000
            }

atmamount = [1000000]


def withdraw():
    y = atmamount[0]
    patron = str(input(print("Current amount in machine: {0} \nEnter your account name:  ".format(y))))
    if patron in accounts:
        x = accounts[patron]
        try:
            amount = int(input(
                print("Hello {0}! \n Your current balance is: {1} \n Enter amount to withdraw: ".format(patron, x))))
            if amount < x and amount < y:
                newbalance = x - amount
                newatmamount = y - amount
                accounts[patron] = newbalance
                atmamount[0] = newatmamount
                print("THIS IS YOUR OFFICIAL RECEIPT")
                print(" Name: {0} \n Balance: {1} \n Amount witdrawn: {2} \n New Balance: {3}".format(patron, x, amount,
                                                                                                      newbalance))
                transaction = str(input("Would you like to make another transaction?: \n Yes \n No \n"))
                if transaction == "Yes" or transaction == "yes":
                    withdraw()
                elif transaction == "No" or transaction == "no":
                    print("GOOD BYE")
            elif amount >= y:
                print("Machine has insufficient funds please try another machine")
                withdraw()
            elif amount > x:
                print("Insufficient funds please deposit more funds to your account")
                withdraw()
            elif amount == x:
                newbalance = x - amount
                newatmamount = y - amount
                accounts[patron] = newbalance
                atmamount[0] = newatmamount
                print("THIS IS YOUR OFFICIAL RECEIPT")
                print(" Name: {0} \n Balance: {1} \n Amount witdrawn: {2} \n New Balance: {3}".format(patron, x, amount,
                                                                                                      newbalance))
                transaction = str(input("Would you like to make another transaction?: \n Yes \n No \n"))
                if transaction == "Yes" or transaction == "yes":
                    withdraw()
                elif transaction == "No" or transaction == "no":
                    print("GOOD BYE")
        except:
            print("Your ATM Card has been eaten for your stupidity. \n"
                  "You can't type letters in the amount you want to withdraw!!!\n")
            accounts.pop(patron)
            withdraw()

    else:
        print("{0} is not in the system database!".format(patron))
        withdraw()


withdraw()





