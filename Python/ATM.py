user_data = {
    '1234':{'name':'Ram','balance':10000},
    '2345':{'name':'Shyam','balance':50000}}

print("----Welcome to Atm----")

user_pin=input("enter your pin: ")

if user_pin in user_data:
    print("Welcome",user_data[user_pin]['name'])

else:
    print("invalid input")

def Menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def Operation(user_pin):
    while True:
        Menu()    
        choose=input("select from 1 to 4:")
  #check balance
        if choose=='1':
            print(f"Your current balance is:",user_data[user_pin]['balance'])
        # deposit
        elif choose=='2':
            deposit_amount=int(input("Enter amount: Rs. "))
            if deposit_amount > 0:
                user_data[user_pin]['balance'] += deposit_amount
                print(f"Your new balance is: Rs. {user_data[user_pin]['balance']}")
            else:
                print("invalid amount")
        # withdraw
        elif choose=='3':
            withdraw_amount=int(input("Enter amount: Rs. "))
            if user_data[user_pin]['balance'] >= withdraw_amount > 0:
                user_data[user_pin]['balance'] -= withdraw_amount
                print(f"Your new balance is: Rs. {user_data[user_pin]['balance']} ")
            else:
                print("insufficient amount")
        #exit
        elif choose=='4':
            print("Thank You!")
            break
        else:
            print("Invalid Choice. Choose from 1 to 5.")

if user_pin in user_data:
    print("Welcome", user_data[user_pin]['name'])
    Operation(user_pin)
else:
    print("Invalid PIN")


