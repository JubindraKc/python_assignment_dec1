#03. Happy Birthday Song for a Friend

def start():
    
    name = input("What is your name?\n")
    print("So, Is it your birthday today?\n")

    ans = input("yes or no?\n")
    if(ans == "yes"):
        yes(name)
    elif(ans == "no"):
        no(name)



def yes(name):
    print("Happy Birthday to",name)
    print("Happy Birthday to You\nMay God Bless You\nCheers! ",name)

def no(name):
    print("Never Mind Then...")

start()
