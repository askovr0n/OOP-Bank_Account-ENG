# Stworze klase główną Bank - a do nich 3 rozne banki: ING, PKO, Santander, oferujace 3 rozne produkty

import random
import sys
import time
import os

class NorthBank:
    """I am creating a core for my banks"""

    day = 1 # One action costs one day
    __days_till_payment = 3
    __payment = random.randint(4000, 5000)
    __cash_flow = 0

    def __init__(self, current_balance, password_change = False):
        self.__current_balance = current_balance
        self.password_change = password_change
        self.__passes = {'artur': '!234'}

    def login_password(self):

        attempts = 0
        attempts_log = 0

        if self.password_change == False:

            for i in range(0, 4):

                login = str(input("Please insert your login: "))  # maybe dictionary ?
                attempts_log += 1

                if login == next(iter(self.__passes)):
                    password = str(input("Please insert your password: "))
                    if password == self.__passes['artur']:
                        print("That's correct, you are welcome :D\n"
                              "What can I do for you ?")
                        break
                    else:
                        attempts += 1
                        print("Try again.\n"
                              "Currently you have:", eval("3-attempts"), " attempts left.")
                        if attempts == 3:
                            print("Your account is blocked, pls call to service desk")
                            sys.exit()
                if attempts_log == 4:
                    print("Try again later")
                    sys.exit()

        elif self.password_change == True:

            attempts_log_1 = 0
            attempts_log = 0

            for i in range(0, 4):

                login = str(input("Please insert your login: "))
                attempts_log += 1

                if login == next(iter(self.__passes)):
                    password = str(input("Please insert your new password: "))
                    if password == self.__passes['artur']:
                        print("That's correct, you are welcome :D\n"
                              "What can I do for you ?")
                        break
                    else:
                        attempts += 1
                        print("Try again.\n"
                              "Currently you have:", eval("3-attempts"), " attempts left.")
                        if attempts == 3:
                            print("Your account is blocked, pls call to service desk")
                            sys.exit()
                if attempts_log == 4:
                    print("Try again later")
                    sys.exit()

            if attempts_log_1 == 4:
                print("Try again later")
                sys.exit()

    def password_manual(self):

        old_password_repeat = str(input("Pls give me your old password:"))
        while old_password_repeat != next(iter(self.__passes.values())):
            print("Something went wrong, try again")
            old_password_repeat = str(input("Pls give me your old password:"))
        else:
            new_password = str(input("Pls give your new password: "))
            self.__passes['artur'] = new_password
            print(f"Your password has been successfully changed into\n {self.__passes['artur']} \nplease log in again")
            self.password_change = True
            time.sleep(3)
            print("--------------------\n")
            self.login_password()

        return self.__passes['artur']

    @property
    def password(self):
        return self.__passes['artur']

    @password.setter
    def password(self, new_password):
        print(f"Your password has been successfully changed into\n {new_password} \nplease log in again")
        self.__passes['artur'] = new_password
        self.password_change = True
        time.sleep(3)
        print("--------------------\n")
        self.login_password()

    def salary(self):
        self.__current_balance += __class__.__payment
        self.__cash_flow += __class__.__payment
        print("4 days have left! Here is your payment: ", __class__.__payment, "!\n", self.__str__())


    def __counting_days(self):

        __class__.day +=1
        __class__.__days_till_payment -= 1

        if __class__.day == 4:
            self.salary()
            __class__.dzien = 1
            __class__.__days_till_payment = 3

    @staticmethod
    def left_days():
        print("Days left to your payment: " + str(__class__.__days_till_payment))

    def which_day(self):

        if self.day == 1:
            days = "Currently it is the " + str(self.day) + "st day.\n"
        elif self.day == 2:
            days = "Currently it is the " +str(self.day) + "nd day.\n"
        elif self.day == 3:
            days = "Currently it is the " + str(self.day) + "rd day.\n"
        else:
            days = "Currently it is the " + str(self.day) + "th day.\n"
        print(days)


    def __str__(self):
        rep = "Your current balance account bank is equal to {} ".format(self.__current_balance)
        return rep

    def get_debet(self):
        self.debet = int(input("Set the value of debet: "))
        self.__counting_days()
        return self.debet

    def payment(self, expense):

        if expense > self.__current_balance:
            return("You can't buy it, go to work or get a loan")

        try:
            if expense >0:
                self.__current_balance -= expense
                __class__.__cash_flow -= expense
                print("You have spent", expense, "dolars\n", self.stan_konta())
            else:
                print("Who is paying with negative money, cmon\n")
        except:
            pass

        self.__counting_days()

    @staticmethod
    def actual_balance():
        print("Your current cash flow balance is equal to {} dollars".format(__class__.__cash_flow))

    @property
    def paycheck(self):
        return __class__.__payment

    @paycheck.setter
    def paycheck(self, new_payment):
        __class__.__payment = new_payment
        self.__counting_days()
        print("\nMy boss has given me bonus. From today I will be earning: {}".format(__class__.__payment))

    def loan(self, money_loaned):

        self.get_debet()
        #idk how to check whether some method/variable was called during current session
        # that's why, user has to input again a debet

        if self.debet > 0: ### OD TEGO ZACZAC

            if self.debet + self.__current_balance < money_loaned:
                print("Go to work, we can't lend you that money")
            else:
                money_loaned = 1.1 * money_loaned
                self.__current_balance += money_loaned
                print("Pls sign it below with your name")
                text_file = open("Loan_contract.txt", "w")
                name = str(input("Write your name: "))
                while name != next(iter(self.__passes)):
                    print("You have made an error, try again please")
                    name = str(input("Write your name: "))
                else:
                    text_file.write("{}\n".format(name))
                    text_file.close()
                    print("Ok, we can lend you that extra money, but you will have to pay extra, exactly:{0:7.2f} dollars".format(money_loaned))
        else:
            if self.__current_balance < money_loaned:
                print("Go to work, we can't lend you that money")
            else:
                money_loaned = 1.1 * money_loaned
                self.__current_balance += money_loaned
                print("Pls sign it below with your name")
                text_file = open("Loan_contract.txt", "w")
                name = str(input("Write your login "))
                while name != next(iter(self.__passes)):
                    print("You have made an error, try again please")
                    name = str(input("Write your name: "))
                else:
                    text_file.write("{}\n".format(name))
                    text_file.close()
                    print("Ok, we can lend you that extra money, but you will have to pay extra, exactly:{0:7.2f} dollars".format(money_loaned))


    #adding to accounts
    def __add__(self, other):
        total_sum_of_money = self.__current_balance + other.current_balance
        return total_sum_of_money

    # if there is a catastrophe
    def __isub__(self, other):
        __catastrophe = ["avalanche", "flood", "fire"]
        id_of_catastrophe = random.randint(0, 2)
        if id_of_catastrophe == 0:
            print("\nOh no, there has been an {}".format(__catastrophe[id_of_catastrophe]))
            print("Unlucky, you have lost {} dollars".format(other))
        elif id_of_catastrophe == 1 or id_of_catastrophe == 2:
            print("\nOh no, there has been a {}".format(__catastrophe[id_of_catastrophe]))
            print("Unlucky, you have lost {} dollars".format(other))

        self.__current_balance -= other
        return __class__(self.__current_balance)


    def statute(self):

        text_file = open("Bank_statute.txt", "r")
        lines = text_file.readlines()

        for i in lines:
            print(lines)

    def logout(self):
        exit()


""" I am adding bank """

class SouthBank():

    """This bank is just to check whether dunder function __add__() works"""
    def __init__(self, current_balance):
        self.current_balance = current_balance

    def __str__(self):
        return "Your current balance in SouthBank is equal to {}".format(self.current_balance)


def main():

    bank1 = NorthBank(5000)
    bank2 = SouthBank(3000)

    bank1.login_password()

    check = random.randint(1, 5)
    other = random.randint(2000, 3000)
    if check == 1:
        bank1 -= other
        print(bank1)
    elif check == 2:
        bank1.paycheck = other + 4000

    choice = None
    while choice != "0":
        print("""
     Your options
     0- logout
     1 - change password
     2 - read the astute of the bank
     3 - check current balance
     4 - current cashflow
     5 - days left to your salary
     6 - what is the day today
     7 - set the value of debet
     8 - make a payment
     9 - get a loan
     10 - cumulated current balance
     11 - current balance in SouthBank
     """)

        choice = input("Wybierasz: ")
        print()

    #logout
        if choice == "0":
            print("You have successfully logged out")
    # password changing
        if choice == "1":
            password_choice = int(input("If you want to change it manually press 0 or 1 if automatically: "))
            if password_choice == 0:
                bank1.password_manual()
            elif password_choice == 1:
                bank1.password = '!qaz'
    # read astute
        if choice == "2":
            bank1.statute()
    # current account balance
        if choice == "3":
            print(bank1)
    # cash flow
        if choice == "4":
            bank1.actual_balance()
    # days till payment
        if choice == "5":
            bank1.left_days()
     # the number of day
        if choice =="6":
            bank1.which_day()
     # debet
        if choice  =="7":
            bank1.get_debet()
    #payment
        if choice == "8":
            value_of_payment = int(input("How much many would you like to spend ? "))
            bank1.payment(value_of_payment)
    #loan
        if choice == "9": ### OD TEGO ZACZAC
            ensure = str(input("Are you sure? If yes write \"y\", if not write \"n\": "))

            if ensure == "y":
                ensure_money = int(input("How much money would you like to borrow? "))
                bank1.loan(ensure_money)

            elif ensure == "n":
                print("It is sad to hear it, unlucky")

            else:
                print("Something went wrong, you have been logged out")
                bank1.logout()
                time.sleep(3)
                print("\n\n\n")
                print("Please log in again")
                bank1.login_password()

        if choice == '10':
            print("Your accumulated current balance is equal to:"  + str(bank1+bank2) + " dollars")

        if choice == "11":
           print(bank2)

main()

