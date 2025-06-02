import sqlite3
import re
import hashlib
import random
from termcolor import colored
from getpass import getpass
import sys
import time
import os

conn=sqlite3.connect('Smart_save.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL ,            
    sec_name TEXT NOT NULL,            
    user_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    account_number TEXT,
    account_bal REAL DEFAULT 0,
    transaction_pin TEXT
        )
''')
cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    amount REAL NOT NULL,
    recipient TEXT DEFAULT 'you',
    sender TEXT DEFAULT 'you',
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id))
""")
def load(talk,dur):
    spinner=['|','/','-','\\']
    duration=dur
    end_time=time.time()+duration
    print(colored(talk,"yellow"),end=' ')
    while time.time()<end_time:
        for symbol in spinner:
            sys.stdout.write(colored(symbol,'yellow'))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
    print('\n')
def console_progress_bar(iteration, total,length, prefix='', suffix='', decimals=1, fill='█', print_end='\r'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n') # Move to the next line when done
    
    
def signup():
    os.system('cls' if os.name=='nt' else '')
    if __name__ == "__main__":
        items = list(range(0, 40))
        l = len(items)

        print("Main-Menu/Sign-Up...")
        # Initial call to print 0% progress
        console_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 60)
        for i, item in enumerate(items):
            time.sleep(0.2) # Simulate some work
            # Update progress bar
            console_progress_bar(i + 1, l, prefix = 'Please wait:', suffix = 'Complete', length = 50)
    time.sleep(3)
    os.system('cls' if os.name=='nt' else '')
    print('='*70)
    print(colored(f"{'SMART SAVE SIGNUP - CREATE NEW ACCOUNT':^70}",'light_blue','on_dark_grey',['bold']))
    print('='*70)
    print("\nPlease provide the following details to create your account.")
    print("-" * 60)

    while True:
        first_name=input(colored('Enter your first name: ','yellow')).strip().title() 
        if not first_name:
            print("first name required")
            continue
        break
    time.sleep(1)
    while True:
        sec_name=input(colored('Enter your last name: ','yellow')).strip().title()
        if not sec_name:
            print("second name required")
            continue
        break
    time.sleep(1)

    while True:
        user_name=input(colored('Enter your username: ','yellow')).strip()
        if not user_name:
            print('user name required')
            continue
        special_characters = '., !@#$%^&*().'
        has_at_least_8_char = len(user_name)>=6
        has_uppercase=any([char.isupper() for char in user_name])
        has_lower = any([char.islower() for char in user_name])
        has_at_least_one_digit = any(char.isdigit() for char in user_name)
        has_special_charcter = [sc for sc in special_characters]
        has_at_least_1_special_character =any(sc in special_characters for sc in user_name)
        if not all([has_at_least_1_special_character,has_at_least_8_char,has_uppercase,has_lower,has_at_least_one_digit]):
            print('username must be at least 6 characters ,has at least one (uppercase,lowercase,digit and at least one special character)')
            continue
        break
    time.sleep(1)

    while True:
        email=input(colored('enter your email (----@gmail.com): ','yellow')).strip()
        if not email:
            print('email required')
            continue    
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        form=re.match(pattern,email)
        if not form:
            print('email not correct .Enter a valid email')
            continue
        break
    time.sleep(1)

    while True:
        password= getpass(colored('Enter your password: ','yellow'))
        password=str(password)
        password=password.strip()
        if not password:
            print('password required')
            continue
        comfirm_password=getpass(colored('renter your password again: ','yellow'))
        comfirm_password=str(comfirm_password)
        comfirm_password=comfirm_password.strip()

    
        if not comfirm_password:
            print(colored('password reqiured for additional comfirmation of Your password','yellow'))
            continue
        elif password!=comfirm_password:
            continue

        

        special_characters = '., !@#$%^&*().'
        has_at_least_8_char = len(password)>=8
        has_uppercase=any([char.isupper() for char in password])
        has_lower = any([char.islower() for char in password])
        has_at_least_one_digit = any(char.isdigit() for char in password)
        has_special_charcter = [sc for sc in special_characters]
        has_at_least_1_special_character =any(sc in special_characters for sc in password)
        if not all([has_at_least_1_special_character,has_at_least_8_char,has_uppercase,has_lower,has_at_least_one_digit]):
            print('password must be at least 8 characters ,has at least one (uppercase,lowercase,digit and at least one special character)')
            continue
        hashed_password=hashlib.sha256(password.encode()).hexdigest()

        break
    try: 
        cursor.execute("""INSERT INTO users(first_name, sec_name, user_name, email, password)VALUES
            (?, ?, ?, ?, ?)""",(first_name,sec_name,user_name,email,hashed_password))
    except sqlite3.IntegrityError as e:
        print('\x1b[3m'+colored('a user with that username already exists!','red'))
    else:    
      
        # print(al[-1])

        conn.commit()
        print('signed up sucessfully')
        acct='50'
        while True:
            for i in range(6):
                number=random.randint(1,9)
                acct+=str(number)
            is_exists=cursor.execute("SELECT * FROM users WHERE account_number=?",(acct,)).fetchone()

            if not is_exists:
                break
            else:
                continue

        os.system('cls' if os.name=='nt' else '')        
        load(f'{user_name} please wait',6)
        print(f'your account number is {acct}')
        while True:
            trans_pin=getpass('Enter your four digit transaction pin: ').strip()

            try:
                int(trans_pin)
            except ValueError: 
                print('\x1b[3m'+colored('transaction pin as to be digits!','red'))
            else: 
               
                if not trans_pin:
                    print('transaction pin required')
                    continue
                elif len (trans_pin)!=4:
                    print('transaction pin as to be four digits')
                    continue
                while True:
                    confirm_trans_pin=getpass('renter your four digit transaction pin: ').strip()   
                    if not confirm_trans_pin:
                        continue
                    break
                if trans_pin != confirm_trans_pin:
                    print('\x1b[3m'+ colored('pin doesn\'t match','red'))
                    continue
                else:
                    trans_pin=hashlib.sha256(str(trans_pin).encode()).hexdigest()
                    cursor.execute("UPDATE users SET transaction_pin=? WHERE user_name=?",(trans_pin,user_name))
                    break
        cursor.execute("UPDATE users SET account_number=? WHERE user_name=?",(acct,user_name))
        last_record=cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1").fetchone()
        # print(last_record)
        print(last_record[0],end="     ")
        print(last_record[1],end="     ")
        print(last_record[2],end="     ")
        print(last_record[3],end="     ")
        print(last_record[4],end="     ")
        print(last_record[7])
        user_id,first_name, sec_name, user_name, email, password,acct_num,acct_bal,pin=last_record
        while True:
            try:
                initial_deposit = float(input('Enter your initial deposit : '))
            except ValueError as e:
                print('\x1b[3m'+colored(f'something went wrong : {e}!','red'))
                continue
            else:
                if initial_deposit<1:
                    print('\x1b[3m'+colored('invalid deposit amount entered!','red'))
                    continue
                else:
                    os.system('cls' if os.name=='nt' else '')
                    load('depositing...',2)
                    os.system('cls' if os.name=='nt' else '')
                    acct_bal+=initial_deposit
                    cursor.execute("UPDATE users SET account_bal=? WHERE id =?",(acct_bal,user_id))
                    available_amt=cursor.execute("SELECT account_bal FROM users WHERE user_name=?",(user_name,)).fetchone()
                    print(colored('Deposited successfully','green'))
                    print(f'your account balance is {acct_bal}')

                    cursor.execute("INSERT INTO transactions (transaction_type, amount, user_id) VALUES (?, ?, ?)", ("Deposit", initial_deposit, user_id))

                    trans=cursor.execute("SELECT * FROM transactions WHERE id=?",(user_id,)).fetchall()
                    # print(trans[-1])
                    last_trans=trans[-1]
                    load('printing reciept',4)
                    print(f'transaction id =>{last_trans[0]}')
                    time.sleep(0.3)
                    print(f'transaction type =>{last_trans[1]}')
                    time.sleep(0.3)
                    print(f'transaction time =>{last_trans[2]}')
                    time.sleep(0.3)
                    print(f'amount =>{last_trans[3]}')
                    time.sleep(0.3)
                    print(f'to =>{last_trans[4]}')
                    time.sleep(0.3)
                    print(f'from =>{last_trans[5]}')
                    print("\n")
                    conn.commit()
                    break
                
        conn.commit()
        load('login',5)
        login()
def trasactions(user):
    os.system('cls' if os.name=='nt' else '')
    if __name__ == "__main__":
        items = list(range(0, 25))
        l = len(items)

        print("Main-Menu/Login/Menu...")
        # Initial call to print 0% progress
        console_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.2) # Simulate some work
            # Update progress bar
            console_progress_bar(i + 1, l, prefix = 'Please wait:', suffix = 'Complete', length = 50)
    time.sleep(3)
    os.system('cls' if os.name=='nt' else '')
    user_id,first_name, sec_name, user_name, email, password,acct_num,acct_bal,pin=user
    print(f'ID:{user_id}    First Name:{first_name}    Last Name:{sec_name}    Username:{user_name}    Account Number:{acct_num}    Account Balance:{acct_bal}')
    print('='*70)
    print(colored(f"{'SMART SAVE PSB - WELCOME ':^70}",'light_green','on_dark_grey',['bold']))
    print('='*70)
    while True:
        print(f'Welcome {user_name} 👋🏼')

        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.View Transaction History")
        print("5.Quit")
        opt = input(colored('from the options above choose the operation you want to perform: ','yellow')).strip()
        
        if opt == '1':
            try:
                amt = float(input('Enter how much you want to deposit into your account: '))
            except ValueError as e:
                print('\x1b[3m'+colored(f'something went wrong : {e}!','red'))
            else:
                if amt<1:
                    print('\x1b[3m'+colored('invalid deposit amount entered!','red'))
                else:
                    os.system('cls' if os.name=='nt' else '')
                    load('depositing...',2)
                    os.system('cls' if os.name=='nt' else '')

                    acct_bal+=amt
                    cursor.execute("UPDATE users SET account_bal=? WHERE user_name =?",(acct_bal,user_name))
                    available_amt=cursor.execute("SELECT account_bal FROM users WHERE user_name=?",(user_name,)).fetchone()
                    print(colored('Deposited successfully','green'))
                    print(f'your account balance is {acct_bal}')

                    cursor.execute("INSERT INTO transactions (transaction_type, amount, user_id) VALUES (?, ?, ?)", ("Deposit", amt, user_id))

                    trans=cursor.execute("SELECT * FROM transactions WHERE user_id=?",(user_id,)).fetchall()
                    # print(trans[-1])
                    last_trans=trans[-1]
                    load('printing reciept',4)
                    print(f'transaction id =>{last_trans[0]}')
                    time.sleep(0.3)
                    print(f'transaction type =>{last_trans[1]}')
                    time.sleep(0.3)
                    print(f'transaction time =>{last_trans[2]}')
                    time.sleep(0.3)
                    print(f'amount =>{last_trans[3]}')
                    time.sleep(0.3)
                    print(f'to =>{last_trans[4]}')
                    time.sleep(0.3)
                    print(f'from =>{last_trans[5]}')
                    print("\n")
                    conn.commit()
            
                
        elif opt=='2':
            try:
                withdraw_amt=float(input("Enter the amount you want to withdraw: "))
            except ValueError as e:
                print('\x1b[3m'+colored(f'something went wrong: {e}!','red'))
            else:
                if withdraw_amt>acct_bal:
                    print('\x1b[3m'+colored('insufficient balance!','red'))
                elif withdraw_amt<1:
                    print('\x1b[3m'+colored('invalid withrawal amount!','red'))
                else:
                    y=4
                    for x in range(4):
                        while True:
                            withdraw_pin=getpass(colored('Enter your transaction pin: ','yellow')).strip()
                            if not withdraw_pin:
                                print(colored('withdraw pin required','red'))
                                continue
                            break
                        if hashlib.sha256(str(withdraw_pin).encode()).hexdigest()==pin:        
                            os.system('cls' if os.name=='nt' else '')
                            load('withdrawing...',4)
                            os.system('cls' if os.name=='nt' else '')
                            acct_bal-=withdraw_amt    
                            cursor.execute("UPDATE users SET account_bal=? WHERE user_name =?",(acct_bal,user_name))
                            available_amt=cursor.execute("SELECT account_bal FROM users WHERE user_name=?",(user_name,)).fetchone()
                            print(colored('Withdrawn Successfully','green'))
                            print(f'you account balance is {acct_bal}')
                            cursor.execute("INSERT INTO transactions (transaction_type, amount, user_id) VALUES (?, ?, ?)", ("Withdrawal", withdraw_amt, user_id))
                            trans=cursor.execute("SELECT * FROM transactions WHERE user_id=?",(user_id,)).fetchall()
                        #  print(trans[-1])
                            last_trans=trans[-1]
                            load('printing reciept',4)
                            print(f'transaction id =>{last_trans[0]}')
                            time.sleep(0.3)
                            print(f'transaction type =>{last_trans[1]}')
                            time.sleep(0.3)
                            print(f'transaction time =>{last_trans[2]}')
                            time.sleep(0.3)
                            print(f'amount =>{last_trans[3]}')
                            time.sleep(0.3)
                            print(f'to =>{last_trans[4]}')
                            time.sleep(0.3)
                            print(f'from =>{last_trans[5]}')
                            print("\n")
                            conn.commit()
                            break

                       
                        else:
                            y-=1
                            print('\x1b[3m'+colored('invalid pin retry','red'))
                            print(f'you have {y} attempts left')
                            # continue
                    else:
                        print('\x1b[3m'+colored('invalid pin','red'))
                        # print('account on cooldown')
                        os.system('cls' if os.name=='nt' else '')

                        cool=20
                        while cool>0:
                            print(f'try again in {cool} seconds')
                            time.sleep(1)
                            cool-=1
                            os.system('cls' if os.name=='nt' else '')

        elif opt=='3':
            recipient_acct_no=input( colored('enter recipient account number: ','yellow')).strip()
            if not recipient_acct_no:
                print('\x1b[3m'+colored('recipient\'s account number required pls!','red'))
            elif len (recipient_acct_no)<8 or len(recipient_acct_no)>8:
                print('\x1b[3m'+colored('invalid account number','red'))
            elif not recipient_acct_no.startswith('50'):
                print('\x1b[3m'+colored('Smart Save account number not in format!','red'))
            elif recipient_acct_no==acct_num:
                print('\x1b[3m'+ colored('opps looks like there is some mix up with the account number!','light_red'))
            else:    
                search_for_recipient=cursor.execute("SELECT * FROM users WHERE account_number=?",(recipient_acct_no,)).fetchone()
                if search_for_recipient:
                    recipient_name=search_for_recipient[1] + ' ' + search_for_recipient[2]
                    try:
                        amt_to_recipient=float(input(f'enter the amount you want to transfer to {recipient_name}: '))
                    except ValueError as e:
                        print('\x1b[3m'+ colored(f'something went wrong {e}!','red'))
                    else:    
                        if amt_to_recipient>acct_bal:
                            print('\x1b[3m'+colored('insufficient balance!','red'))
                        elif amt_to_recipient<1:
                            print('\x1b[3m'+colored('invalid transfer amount!','red'))
                        else:
                            os.system('cls' if os.name=='nt' else '')
                            load('please wait',3)
                            os.system('cls' if os.name=='nt' else '')
                            recipient_acct_bal=search_for_recipient[-2]
                            
                            k=4
                            for i in range(4):
                                while True:
                                    pin_validation=input(colored('enter your pin: ','yellow')).strip()
                                    if not pin_validation:
                                        print(colored(f'pin required to do transfer to {recipient_name}','red'))
                                        continue
                                    else:
                                        break
                                        
                                            
                                if hashlib.sha256(str(pin_validation).encode()).hexdigest()==pin:
                                    recipient_acct_bal+=amt_to_recipient
                                    acct_bal-=amt_to_recipient
                                    cursor.execute("UPDATE users SET account_bal=? WHERE account_number=? ",(recipient_acct_bal,recipient_acct_no))
                                    cursor.execute("UPDATE users SET account_bal=? WHERE user_name =?",(acct_bal,user_name))
                                    cursor.execute("INSERT INTO transactions (transaction_type, amount, user_id,recipient) VALUES (?, ?, ?, ?)", ("Transfer", amt_to_recipient, user_id, recipient_acct_no))
                                    print(colored('Transfer Successful','green'))
                                    print(f'you account balance is {acct_bal}')

                                    cursor.execute("INSERT INTO transactions (transaction_type, amount, user_id,sender) VALUES (?, ?, ?, ?) ", ("Deposit", amt_to_recipient, search_for_recipient[0], acct_num))                            
                                    trans=cursor.execute("SELECT * FROM transactions WHERE user_id=?",(user_id,)).fetchall()
                                    # print(trans[-1])
                                    last_trans=trans[-1]

                                    load('printing reciept', 4)
                                    

                                    # for j in last_trans:

                                    print(f'transaction id =>{last_trans[0]}')
                                    time.sleep(0.3)
                                    print(f'transaction type =>{last_trans[1]}')
                                    time.sleep(0.3)
                                    print(f'transaction time =>{last_trans[2]}')
                                    time.sleep(0.3)
                                    print(f'amount =>{last_trans[3]}')
                                    time.sleep(0.3)
                                    print(f'to =>{last_trans[4]}')
                                    time.sleep(0.3)
                                    print(f'from =>{last_trans[5]}')
                                    print('\n')
                                    conn.commit()
                                    
                                    break
                                else:
                                    k-=1
                                    print('\x1b[3m'+colored('invalid pin retry','red'))
                                    print(f'you have {k} attempts left')
                                    # continue
                                # i+=1
                            else: 
                                print('\x1b[3m'+colored('invalid pin!','red'))
                                # print('account on cooldown')
                                os.system('cls' if os.name=='nt' else '')

                                cool=20
                                while cool>0:
                                    print(f'try again in {cool} seconds')
                                    time.sleep(1)
                                    cool-=1
                                    os.system('cls' if os.name=='nt' else '')

                else:
                    print('\x1b[3m'+colored("account number not found!",'red'))
                
            
        elif opt=='4':
            os.system('cls' if os.name=='nt' else '')
            load('printing transactions please wait', 7)          
            trans_for=cursor.execute("SELECT * FROM transactions WHERE user_id=?",(user_id,)).fetchall()
            # print(trans_for)
            if trans_for:
                for j in trans_for:
                    print(f'transaction id =>{j[0]}')
                    time.sleep(0.1)
                    print(f'transaction type =>{j[1]}')
                    time.sleep(0.1)
                    print(f'transaction time =>{j[2]}')
                    time.sleep(0.1)
                    print(f'amount =>{j[3]}')
                    time.sleep(0.1)
                    print(f'to =>{j[4]}')
                    time.sleep(0.1)
                    print(f'from =>{j[5]}')
                    print('\n')
            else:
                print(colored("Could not retrieve transaction receipt.", "red"))
        elif opt=='5':
            print("bye 👋🏼 hope we see you next time")
            break
        else:
            print('\x1b[3m'+colored('invalid option! ','red'))
            print('\x1b[3m'+colored('btw option 1 to 5 choose the transaction you want to perform \nfrom the above options ','yellow'))


            


def login():
  
    os.system('cls' if os.name=='nt' else '')
    if __name__ == "__main__":
        items = list(range(0, 25))
        l = len(items)

        print("Main-Menu/Login...")
        # Initial call to print 0% progress
        console_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.2) # Simulate some work
            # Update progress bar
            console_progress_bar(i + 1, l, prefix = 'loging in:', suffix = 'Complete', length = 50)
    # load('please wait', 5)
    time.sleep(2)
    os.system('cls' if os.name=='nt' else '')
    # os.system('cls' if os.name=='nt' else '')
    print('='*70)
    print(colored(f"{'SMART SAVE LOGIN - WELCOME ':^70}",'light_cyan','on_dark_grey',['bold']))
    print('='*70)
    while True:
        user_name=input(colored('Enter your username: ','yellow')).strip()
        if not user_name:
            print('user name required')
            continue
        break
    while True:
        password= getpass(colored('Enter your password: ','yellow'))
        password=str(password)
        password=password.strip()
        if not password:
            print('password required')
            continue
        break
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    user = cursor.execute("SELECT * FROM users WHERE user_name= ? AND password = ? ",(user_name,hashed_password)).fetchone()
    if user != None:
        print(colored('login successful','green'))
        load('logining to dashboard',5)
        
        # print(user)
        trasactions(user)

    else:
        print('\x1b[3m' + colored('invalid username or password!','red'))
def forget_password():
    os.system('cls' if os.name=='nt' else '')
    if __name__ == "__main__":
        items = list(range(0, 25))
        l = len(items)

        print("Main-Menu/Forgot-Password...")
        # Initial call to print 0% progress
        console_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.2) # Simulate some work
            # Update progress bar
            console_progress_bar(i + 1, l, prefix = 'Please wait:', suffix = 'Complete', length = 50)
    # load('please wait', 5)
    time.sleep(2.5)
    os.system('cls' if os.name=='nt' else '')
    print('='*70)
    print(colored(f"{'FORGOT PASSWORD - RESET':^70}",'grey','on_black',['bold']))
    print('='*70)
    while True:
        email=input(colored('enter your email (----@gmail.com): ','yellow')).strip()
        if not email:
            print('email required')
            continue    
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        form=re.match(pattern,email)
        if not form:
            print('email not correct .Enter a valid email')
            continue
        break  
    while True:
        user_id=input(colored('Enter your id: ','yellow')).strip()
        if not user_id:
            print('user name required')
            continue
        break
    while True:
        username=input(colored('Enter your username: ','yellow')).strip()
        if not username:
            print('user name required')
            continue
        break
    find=cursor.execute("SELECT * FROM users WHERE id=? AND user_name=? AND email=? ",(user_id,username,email)).fetchone()
    if find:
        while True:
            password= getpass(colored('Enter your new  password: ','yellow'))
            password=str(password)
            password=password.strip()
            if not password:
                print('password required')
                continue
            comfirm_password=getpass(colored('renter your new password again: ','yellow'))
            comfirm_password=str(comfirm_password)
            comfirm_password=comfirm_password.strip()

        
            if not comfirm_password:
                print(colored('password reqiured for additional comfirmation of Your password','yellow'))
                continue
            elif password!=comfirm_password:
                continue

            

            special_characters = '., !@#$%^&*().'
            has_at_least_8_char = len(password)>=8
            has_uppercase=any([char.isupper() for char in password])
            has_lower = any([char.islower() for char in password])
            has_at_least_one_digit = any(char.isdigit() for char in password)
            has_special_charcter = [sc for sc in special_characters]
            has_at_least_1_special_character =any(sc in special_characters for sc in password)
            if not all([has_at_least_1_special_character,has_at_least_8_char,has_uppercase,has_lower,has_at_least_one_digit]):
                print('password must be at least 8 characters ,has at least one (uppercase,lowercase,digit and at least one special character)')
                continue
            hashed_password=hashlib.sha256(password.encode()).hexdigest()

            break
        cursor.execute("UPDATE users SET password=? WHERE user_name=? ",(hashed_password,username))
        print('chamged successfully')
        conn.commit()
        login()
        
    else:
        print('\x1b[3m' +colored('invalid email, id, or username !','red'))
# login()
no='50699563'
meact='50187944'
kidd0='50833258'




def main():
    os.system('cls' if os.name=='nt' else '')
    if __name__ == "__main__":
        items = list(range(0, 50))
        l = len(items)

        print("Main-Menu...")
        # Initial call to print 0% progress
        console_progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 100)
        for i, item in enumerate(items):
            time.sleep(0.2) # Simulate some work
            # Update progress bar
            console_progress_bar(i + 1, l, prefix = 'Welcome:', suffix = 'Complete', length = 100)
    time.sleep(2)
    os.system('cls' if os.name=='nt' else '')
    print('='*70)
    print(colored(f"{'*Smart Save*':^70}",'light_magenta','on_dark_grey',['bold']))
    print('='*70)

    while True:
        print("1.Signup")
        print("2.Login")
        print("3.Forgot Password ?")
        print("4.Quit")
        main_options=input(colored("Welcome to Smart Save bank\npress 1 to signup \npress 2 if you've signed up already \npress 3 for forgot password option \npress 4 to quit :> ",'yellow'))
        if main_options=='1':
            signup()
        elif main_options=='2':
            login()
        elif main_options=='3':
            forget_password()
        elif main_options=='4':
            break
        else:
            print("\x1b[3m" + colored('wrong option!','red')+ '\x1b[0m')
            time.sleep(3)
            os.system('cls' if os.name=='nt' else '')

            continue
try:
    main()
except Exception as e:
    print(f'something went wrong {e}')
finally:
    conn.close()
# forget_password()

# kammy=50666779 