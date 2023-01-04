# Banking System
#Creating the account
creatingacc = []
name = input("Enter Name: ")
creatingacc.append(name)
Dob = input("Enter Date of birth(DD,MM,YYYY): ")
creatingacc.append(Dob)
Telephone_num = input("Enter Phone Number: ")
creatingacc.append(Telephone_num)
Location = input("Enter Location: ")
creatingacc.append(Location)
#Generating the Account Number
account_num =[]
a = name[:2]
b = Telephone_num[:2]
c = Location[:-2]
d = Dob[:3]
account_num.append(a)
account_num.append(b)
account_num.append(c)
account_num.append(d)
str = " "
y = tuple(account_num)
x=str.join(y)
my_account_num = x.replace(" ","")
 

class Bank_Account:
    def __init__(slip):
        slip.balance = 0

    def Deposit(slip):
     amount = float(input("Enter Amount you want to deposit: "))
     slip.balance += amount
     print(f"\n Amount deposited{amount}")

    def Withdraw(slip):
     amount = float(input("Enter amount you want to with draw: "))
     if slip.balance >= amount:
        slip.balance -= amount
        print(f"\n You Withdrew {amount}")
     else:
        print(f"\n Insufficient balance ")
    def check_balnce(slip):
     print(f"\n Available Balance is {slip.balance}")
s = Bank_Account()

    



Congrtsint = "Congratulations, you have sucessfully created your bank account."
print(Congrtsint)
procceed = input("Would you like to proceed to the following services? ")
while procceed == "yes":
    option_1 = input("Please Select the following Options:\n1. Account Services\n2. Transfer \n")
    if option_1 =="Account Services" or option_1 == "1":
      option_Act_1 = input("Account Services\nPlease Select the following Options\n1.Check Balance\n2.Request details\n")
      if option_Act_1 == "Check Balance" or option_Act_1 == "1":
        print(s.check_balnce())
      elif option_Act_1 == "Request details" or option_Act_1 =="2":
        print(f"Your account details is as follows {creatingacc} and your account number is => {my_account_num}")
    
    if option_1 == "Transfer" or option_1 == "2":
      option_trs_1 = input("Transfer\nPlease Select the following Options\n1.Deposit\n2.Withdraw\n")
      if option_trs_1 == "Deposit" or option_trs_1 == "1":
        print(s.Deposit())
      elif option_trs_1 =="Withdraw" or option_trs_1 == "2":
        print(s.Withdraw())
        
    procceed = input("Would you like to continue? ")
    if procceed == "no":
        print("Have a nice day")
        break
        
    















