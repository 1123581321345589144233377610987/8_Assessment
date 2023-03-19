errorfile = "accounts.txt"
try:
    Accounts = open('accounts.txt','r')
    errorfile = "over90.txt"
    Due = open('over90.txt','r')
    accounts = Accounts.readlines()
    due = Due.readlines()
    Accounts.close()
    Due.close()
    count = 0
    for i in due:
        due[count] = due[count].strip('\n')
        count += 1
    for i in accounts:
        I = i.split(',')
        if I[0] in due:
            print(i.strip("\n)
except FileNotFoundError:
    print(f"{errorfile} does not exist.")
