print("Health Management System")
def getdate():
    import datetime
    return datetime.datetime.now()
def data_input(a):
    if a==1:
        print("Do you want to lock exercise or diet? Press 1 for exercise and 2 for diet :")
        log=int(input())
        if log ==1:
            print("Enter your data :")
            n=str(input())
            f=open("samhita_exercise.txt","a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
        elif log==2:
            print("Enter your data :")
            n = str(input())
            f = open("samhita_diet.txt", "a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
    if a==2:
        print("Do you want to log exercise or diet? Press 1 for exercise and 2 for diet :")
        log = int(input())
        if log == 1:
            print("Enter your data :")
            n = str(input())
            f = open("subhrayan_exercise.txt", "a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
        elif log == 2:
            print("Enter your data :")
            n = str(input())
            f = open("subhrayan_diet.txt", "a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
    if a==3:
        print("Do you want to log exercise or diet? Press 1 for exercise and 2 for diet :")
        log = int(input())
        if log == 1:
            print("Enter your data :")
            n = str(input())
            f = open("rajeswari_exercise.txt", "a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
        elif log == 2:
            print("Enter your data :")
            n = str(input())
            f = open("rajeswari_diet.txt", "a")
            f.write(str(getdate()))
            f.write(":")
            f.write(n)
            f.write("\n")
            f.close()
def retrieve(b):
    if b==1:
        print("Retrieve exercise data press 1 and for diet data press 2")
        cno=int(input())
        if cno==1:
            f = open("samhita_exercise.txt", "r")
            content = f.read()
            print(content)
        elif cno==2:
            f = open("samhita_diet.txt", "r")
            content = f.read()
            print(content)
    elif b==2:
        print("Retrieve exercise data press 1 and for diet data press 2")
        cno = int(input())
        if cno == 1:
            f = open("subhrayan_exercise.txt", "r")
            content = f.read()
            print(content)
        elif cno == 2:
            f = open("subhrayan_diet.txt", "r")
            content = f.read()
            print(content)
    elif b==3:
        print("Retrieve exercise data press 1 and for diet data press 2")
        cno = int(input())
        if cno == 1:
            f=open("rajeswari_exercise.txt", "r")
            content=f.read()
            print (content)
        elif cno == 2:
            f = open("rajeswari_diet.txt", "r")
            content = f.read()
            print (content)
choice=int(input("Do you want to log in or retrieve? Press 1 to log in ,2 to retrive :"))
if choice==1:
    c=int(input("Enter which client you want? press 1 for Samhita,2 for Subhrayan,3 for Rajeswari:"))
    data_input(c)
else:
    c = int(input("Enter which client you want? press 1 for Samhita,2 for Subhrayan,3 for Rajeswari:"))
    retrieve(c)
