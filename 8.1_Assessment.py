afile = "accounts.txt"
odfile = "over90.txt"
try:
    Accounts = open(afile,'r')
    try:
        Due = open(odfile,'r')
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
                print(i.strip("\n"))
    except FileNotFoundError:
        print(f"{odfile} does not exist.")
except FileNotFoundError:
    print(f"{afile} does not exist.")
