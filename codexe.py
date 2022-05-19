import os

print('----------------------   Call of Duty®: Black Ops 2  ---------------------->')
print('                           __________  __________')
print('                          |          ||          |')  
print('                          |          ||          |')  
print('                           \         ||         /')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                            |        ||        |')
print('                           /         ||         \ ')
print('                          |          ||          |')   
print('                          |__________||__________|\n')





c = os.path.dirname(os.path.abspath(__file__)) + '/short'

try:
    os.mkdir(c)
except:
    pass
    

print('\n setup:')

print('[I] - this file should be in the same directory as the exe files')
print('[II] - put shortcuts of each exe file in the ./short folder  ')
print('choose one option :')

def oof():
    def foo():
        choice = 0
        way = 0
        while True:
            while True:
                print('     [1]singleplayer')
                print('     [2]multiplayer')
                print('     [3]zombies')
                choice = input('type :      ')
                try:
                    int(choice)
                    break
                except:
                    print('\n -- wrong input\n')
            choice = int(choice)
            if choice in (1,2,3):
                break
            else:
                print('\n -- wrong input\n')
        if choice in (2,3):
            while True:
                while True:
                    print('     [1]online')
                    print('     [2]offline')
                    way = input('type :      ')
                    try:
                        int(way)
                        break
                    except:
                        print('\n -- wrong input\n')
                way = int(way)
                if way in (1,2):
                    break
                else:
                    print('\n -- wrong input\n')

        run = [choice,way]
        print(run)
        return run


    def regret():
         while True:
            a = input('[0]homepage | [1]close ') 
            if a == '0':
                oof()
                break
            elif a == '1':
                exit()
            else:
                print('wrong input \n')    


    run = foo()

    if run[0] == 1:
        prpt = None
        while True:  
            print('run single-player ?   [0]yes | [1]no')
            prpt = input()
            if prpt == '0' or prpt == '':
                prpt = True
                break
            elif prpt == '1':
                prpt = False
                break
            else:
                print('\n -- wrong input\n')

        if prpt == False:
           regret()
        elif prpt == True :
            os.startfile('D:/CallofDuty-BlackOps2/short/t6sp.exe.lnk')
            exit()


    
    elif run[0] == 2:
        if run[1] == 1:
            while True :
                a = None 
                print('run online multiplayer       [1]yes || [2]no')
                a = input('...  ')
                if a == '1':
                    os.startfile('D:\CallofDuty-BlackOps2\short/t6mp.exe.lnk')
                    exit()   
                elif a == '2':
                    regret()

        elif run[1] == 2:
             while True :
                a = None 
                print('run offline multiplayer?       [1]yes || [2]no')
                a = input('...  ')
                if a == '1':
                    os.startfile('D:\CallofDuty-BlackOps2\short/t6mp-MultiplayerOffline.exe.lnk')
                    exit()
                elif a == '2':
                    regret()

    
    elif run[0] == 3:
        if run[1] == 1:
            while True :
                a = None 
                print('run online zombies?       [1]yes || [2]no')
                a = input('...  ')
                if a == '1':
                    os.startfile('D:\CallofDuty-BlackOps2\short/t6zm.exe.lnk')
                    exit()   
                elif a == '2':
                    regret()

        elif run[1] == 2:
             while True :
                a = None 
                print('run offline zombies?       [1]yes || [2]no')
                a = input('...  ')
                if a == '1':
                    os.startfile('D:\CallofDuty-BlackOps2\short/t6zm-ZombiesOffline.exe.lnk')
                    exit()
                elif a == '2':
                    regret()
    else:
        print('error occured')
        exit()

oof()   