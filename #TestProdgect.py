#Test
#Импорт модулей
import os
import time

os.environ["opswersionadversionanv"] = str(12763591872673812)
#Перременная окружения
valuecheck = os.environ["opswersionadversionanv"]
#Лого
print("Welcome to TPO OS 1.2")
print("Python for linux")

logo1 = "------TPO OS-------"
logo2 = "--VERSION: 1.2 ----"
logo3 = "--CONFIG: STANDART-"
logo4 = "-------------------"
time.sleep(3)
#Проверка версии
checktrialversion1 = input("Windows = 1/ Linux Fedora = 2:")
if checktrialversion1 == "1":
    if valuecheck == "12763591872673812":
        print("System is registered!")
        time.sleep(1)
    else:
        print("-----YOU USED HACK VERSION!-----")
        time.sleep(2)
        exit(404)


name = input("Please Enter you login:")
password = input("Please Enter you password:")
passkey = input("Enter you passkey:")

namedost = ["Ivan", "TEST"]
passdost = ["132324", "114123", "132435", "TESTUPUSER"]
passkeydost = [990099, 991199, 992299,"TEST"]

if name in namedost:
    print("Name valid!")
else:
    print("Name invalid!")
    exit()
if password in passdost:
    print("password valid!")
else:
    exit()


while True:
    command = input("Enter terminal command:")
    if command == "version":
        print(logo1)
        print(logo2)
        print(logo3)
        print(logo4)
    if command == "help":
        print("<--------------------HELP PAGE--------------------->")
        print("<--version         | informations of system        >")
        print("<--graficsys.help  | grafic info                   >")
        print("<--grafic_test.sys | grafic test                   >")
        print("<--EXIT            | Exit                          >")
        print("<-------------------------------------------------->")
        time.sleep(1)
    if command == "graficsys.help":
        print("|----------------GRAF 2.0 HELP PAGE----------------|")
        print("|---DRIVER BY: IVAN SHEGLOV------------------------|")
        print("|---POWER BY: TIPOLIST TEAM------------------------|")
        print("|--------------------------------------------------|")
        time.sleep(1)
    if command == "grafic_test.sys":
        print("|=====================TEST PAGE====================|")
        print("----------------------------------------------------")
        print("____________________________________________________")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("(((((((((((((((((((((((((())))))))))))))))))))))))))")
        print("!!!!!!@@@@@@######$$$$$$%^^^^^^&&&&&&******{[}]/?., ")
        print("qwertyuiopasdfghjklzxcvbnm;'________________________")
        print(" 1 2 3 4 5 6 7 8 9 0        ________________________")
        time.sleep(1)
    if command == "PUFSER":
        print("Welcome in P.U.F.S.E.R. menu")
        pufserm = input("Please enter you name:")
        if pufserm == "PUFUSER":
            print("Welcome PUFUSER")
            print("--------------------MENU------------------")
            print("---USER NAME: IVAN, TEST               ---")
            print("---PASSWORD : 132324, 114123           ---")
            print("------------------------------------------")
    if command == "EXIT":
        exit1 = input("Are you sure? Y/n:")
        if exit1 == "Y":
            exitsure = input("Are you sure? Yes/no:")
            if exitsure == "Demo_logoui.123":
                print("--------------------------------------------")
                print("---------------WELCOME USER-----------------")
                print("------------USER_COSTUME_NAME---------------")
                print("--------------------------------------------")
            if exitsure == "Demo_logoutui.123":
                print("--------------------------------------------")
                print("------------------STAND BY------------------")
                print("--------------------:(----------------------")
            if exitsure == "Yes":
                print("EXIT")
                time.sleep(1)
                exit()
        else:
            print("GoodLuck!")
    if command == "tpostats":
        print("|-----------------------TPO.RESRORE-----------------------|")
        print("|---/reset = reset system                              ---|")
        print("|---/version = reset version                           ---|")
    if command == "game1":
        game1 = input("End word: Bow")
        game2 = input("End word: cott")
        game3 = input("End word: Pla")
        if game1 == "l":
            print("+")
        if game2 == "on":
            print("+")
        if game3 == "in":
            print("+")
    