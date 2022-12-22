import sys
import random


class ATM:
    def __init__(self, name, pin, account, account_bal=0):
        self.name = name
        self.pin = pin
        self.account = account
        self.account_bal = account_bal

    def check_pin(self):
        print()
        print(f"""
         **************************                  
         ||   Your pin is {self.pin}   ||
         **************************
        """)
        print()

    def exit(self):
        while True:
            trans = input("Do you want to do any transaction?(y/n): ")
            if trans == "y":
                atm.transaction()
            elif trans == "n":
                print("""
                   ******************************************                    
                   ||   Thank you for choosing SAZBANK!    ||
                   ******************************************
                """)
                sys.exit()
                break
            else:
                print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
                print()


    def bal_inquiry(self):
        print()
        print(f"""
         **********************************                  
         ||   Available balance: ₱{self.account_bal}   ||
         **********************************
        """)
        print()

    def withdraw(self):
        opt = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        while True:
            try:
                amt = input(""" 
          *****************************
          ||          Select Amount: ||
          ||                         ||
          ||  [] 10         60  []   ||
          ||  [] 20         70  []   ||
          ||  [] 30         80  []   ||
          ||  [] 40         90  []   ||
          ||  [] 50         100 []   ||
          *****************************
                """)
                for x in opt:
                    if int(amt) < self.account_bal:
                        if int(amt) == x:
                            self.account_bal -= int(amt)
                            print()
                            print(f"""
          ***************************************************               
          ||   You have withdrawn ₱{amt} from your account.   ||
          ***************************************************
                            """)
                            print(f"\t\t  ")
                            atm.print_receipt()
                            atm.exit()
                    else:
                        print()
                        print("\t\t Insufficient Funds!")
                        break
            except ValueError:
                print("\t\t Invalid Input!")


    def print_receipt(self):
        print(f"""
          ***********************************************
          ||    Transaction is now complete.           ||              
          ||    Transaction number:{random.randint(10000, 1000000)}
          ||    Account holder: {self.name.upper()}                  
          ||    Account number: {self.account}                 
          ||    Remaining balance: ₱{self.account_bal}                   
          ||                                           ||
          ||    Thanks for choosing us as your bank    ||              
          ***********************************************
                         """)

    def transaction(self):
        print("""
            TRANSACTION 
          ****************************
          ||    Menu:               ||
          ||    1. Check PIN        ||
          ||    2. Balance Inquiry  ||
          ||    3. Withdraw         ||
          ||    4. Exit             ||
          ****************************
        """)
        while True:
            try:
                option = int(input("\t\t Enter 1, 2, 3 or 4: "))
            except:
                print("\t\t Error: Enter 1, 2, 3 or 4 only!\n")
                print()
                continue
            else:
                if option == 1:
                    atm.check_pin()
                elif option == 2:
                    atm.bal_inquiry()
                elif option == 3:
                    atm.withdraw()
                elif option == 4:
                    sys.exit()


while True:
    register = input("""
          ******************************************                    
          ||  Welcome to                          ||
          ||                                      ||
          ||           - S A Z B A N K -          ||
          ||                                      ||
          ||          We have your money!         ||
          ||                                      ||
          || [1] create new account               ||
          ******************************************
              """)

    if register == "1":
        name = input("""
          ******************************************                    
          ||   Enter Name:                        ||
          ******************************************
                            """)
        while True:
            try:
                pin = input("""
          ******************************************                    
          ||   Enter 4-digit pin:                 ||
          ******************************************
                                   """)
                if len(pin) > 4:
                    print("""
          Please enter 4-digit pin!""")
                elif len(pin) < 4:
                    print("""
          Please enter 4-digit pin!""")
                else:
                    break
            except ValueError:
                print("Please input numerical values only")
        print("""
          ******************************************                    
          ||                                      ||
          ||    Your account has been created.    ||
          ||       account no: 1234567890         ||
          ||                                      ||
          ||    An amount of ₱1000.00 has been    ||
          ||   added to your account as a bonus.  ||
          ||                                      ||
          ******************************************
     """)
        account = 1234567890
        account_bal = 1000
        atm = ATM(name, pin, account, account_bal)
        break
    else:
        print("""
              Wrong input!""")
        # print(atm.__dict__) check values
        # {'name': 'karlo jay amistoso', 'pin': '1234', 'account': 1234567890, 'account_bal': 1000}
atm.exit()
