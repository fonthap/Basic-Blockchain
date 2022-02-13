from math import fabs
from block  import BlockchaininApp
import database
from sys import exit


blockchainInApp = BlockchaininApp()

x = database.select_db()
j = 0
for i in x:
    if j == 0:
        blockchainInApp.new_block(previous_hash=i[4])
        j = 1
    else:
        blockchainInApp.new_transaction(i[0], i[1], i[2],i[3])
        blockchainInApp.new_block()

def checkdata():
    print('{:-<30}'.format(' '))
    print('{:^30}'.format('Data Verification'))
    print('{:-<30}'.format(' '))
    for round in range(len(blockchainInApp.chain)):
        hashchain = blockchainInApp.chain[round].get('previous_hash')
        hashdata = ''
        tmp = str(round+1)
        x = database.selecthash_db((tmp))
        for i in x:
            hashdata = i[0]
        if hashchain == hashdata:
            print('   Data block %d is correct' % round)
        else:
            print('   Data block %d is not correct' % round)
    print('{:-<30}'.format(' '))

def inputdata():
    print('{:-<70}'.format(' '))
    print('{:^70}'.format('Team'))
    print('{:-<70}'.format(' '))
    print('{:<15}{:<25}{:<25}'.format('','1 : BOOM Esports','5 : OB.Neon'))
    print('{:<15}{:<25}{:<25}'.format('','2 : Fnatic','6 : Execration'))
    print('{:<15}{:<25}{:<25}'.format('','3 : T1','7 : Motivate.Trust Gaming'))
    print('{:<15}{:<25}{:<25}'.format('','4 : Team SMG','8 : TNC Predator'))
    print('{:-<70}'.format(' '))
    print ("Select team")
    tmp = True
    while (tmp):
        team1 = input()
        if(team1 == '1' or team1 == '2'or team1 == '3'or team1 == '4'or team1 == '5'or team1 == '6'or team1 == '7'or team1 == '8'):
            tmp = False
        else:
            print("Try again")

    print ("Select team") 
    tmp = True
    while (tmp):
        team2 = input()
        if(((team1 == '1' and team2 != '1') and (team2 == '2' or team2 == '3'or team2 == '4'or team2 == '5'or team2 == '6'or team2 == '7'or team2 == '8'))
        or ((team1 == '2' and team2 != '2') and (team2 == '1' or team2 == '3'or team2 == '4'or team2 == '5'or team2 == '6'or team2 == '7'or team2 == '8'))
        or ((team1 == '3' and team2 != '3') and (team2 == '2' or team2 == '1'or team2 == '4'or team2 == '5'or team2 == '6'or team2 == '7'or team2 == '8'))
        or ((team1 == '4' and team2 != '4') and (team2 == '2' or team2 == '3'or team2 == '1'or team2 == '5'or team2 == '6'or team2 == '7'or team2 == '8'))
        or ((team1 == '5' and team2 != '5') and (team2 == '2' or team2 == '3'or team2 == '4'or team2 == '1'or team2 == '6'or team2 == '7'or team2 == '8'))
        or ((team1 == '6' and team2 != '6') and (team2 == '2' or team2 == '3'or team2 == '4'or team2 == '5'or team2 == '1'or team2 == '7'or team2 == '8'))
        or ((team1 == '7' and team2 != '7') and (team2 == '2' or team2 == '3'or team2 == '4'or team2 == '5'or team2 == '6'or team2 == '1'or team2 == '8'))
        or ((team1 == '8' and team2 != '8') and (team2 == '2' or team2 == '3'or team2 == '4'or team2 == '5'or team2 == '6'or team2 == '7'or team2 == '1'))):
            team1 = nameteam(team1)
            team2 = nameteam(team2)
            tmp = False
        else:
            print("Try again")

    print ("Enter score team1")
    tmp = True
    while (tmp):
        score1 = input()
        if(score1 == '0' or score1 == '1' or score1 == '2'):
            tmp = False
        else:
            print("Try again")

    print ("Enter score team2")
    tmp = True
    while (tmp):
        score2 = input()
        if((score1 == '0' and score2 == '2') 
        or (score1 == '1' and score2 == '2') 
        or (score1 == '2' and score2 == '0')
        or (score1 == '2' and score2 == '1')):
            tmp = False
        else:
            print("Try again")

    score = score1 + " - " + score2
    blockchainInApp.new_transactionindatabase(team1,team2,score)
    blockchainInApp.new_blockindatabase()
    print("Save data success")

def nameteam(team):
    if(team == '1'):
        return 'BOOM Esports'
    elif(team == '2'):
        return 'Fnatic'
    elif(team == '3'):
        return 'T1'
    elif(team == '4'):
        return 'Team SMG'
    elif(team == '5'):
        return 'OB.Neon'
    elif(team == '6'):
        return 'Execration'
    elif(team == '7'):
        return 'Motivate.Trust Gaming'
    else:
        return 'TNC Predator'


def dataresult():
    print('{:-<108}'.format(' '))
    print('{}{:>25}{:>28}{:>15}{:>35}{:>5}'.format('|','Team1','Team2','Score','Timestamp','|'))
    print('{:-<108}'.format(' '))
    for round in range(len(blockchainInApp.chain)):
        if round >=1 :
            transactions = blockchainInApp.chain[round].get('transactions')
            team1 = transactions[0].get('Team1')
            team2 = transactions[0].get('Team2')
            score = transactions[0].get('Score')
            time =  transactions[0].get('timestamp')
            print('{}{:>25}{:>28}{:>15}{:>35}{:>5}'.format('|',team1,team2,score,time,'|'))
    print('{:-<108}'.format(' '))

def findteam():
    print('{:-<70}'.format(' '))
    print('{:^70}'.format('Team'))
    print('{:-<70}'.format(' '))
    print('{:<15}{:<25}{:<25}'.format('','1 : BOOM Esports','5 : OB.Neon'))
    print('{:<15}{:<25}{:<25}'.format('','2 : Fnatic','6 : Execration'))
    print('{:<15}{:<25}{:<25}'.format('','3 : T1','7 : Motivate.Trust Gaming'))
    print('{:<15}{:<25}{:<25}'.format('','4 : Team SMG','8 : TNC Predator'))
    print('{:-<70}'.format(' '))
    

    print ("Select team")
    tmp = True
    while (tmp):
        team = input()
        if(team == '1' or team == '2'or team == '3'or team == '4'or team == '5'or team == '6'or team == '7'or team == '8'):
            team = nameteam(team)
            tmp = False
        else:
            print("Try again")

    print('{:-<70}'.format(' '))
    print('{:-<108}'.format(' '))
    print('{}{:>25}{:>28}{:>15}{:>35}{:>5}'.format('|','Team1','Team2','Score','Timestamp','|'))
    print('{:-<108}'.format(' '))
    for round in range(len(blockchainInApp.chain)):
        if round >=1 :
            transactions = blockchainInApp.chain[round].get('transactions')
            team1 = transactions[0].get('Team1')
            team2 = transactions[0].get('Team2')
            score = transactions[0].get('Score')
            time =  transactions[0].get('timestamp')
            if team1 == team  or team2 == team:
                print('{}{:>25}{:>28}{:>15}{:>35}{:>5}'.format('|',team1,team2,score,time,'|'))
    print('{:-<108}'.format(' '))

if __name__ == '__main__':

    while True:
        print('{:-<50}'.format(' '))
        print('{:^50}'.format('Assignment 1'))
        print('{:-<50}'.format(' '))
        print('{:15}{:<}'.format('','1 : Add Block'))
        print('{:15}{:<}'.format('','2 : Show  All Data'))
        print('{:15}{:<}'.format('','3 : Check Data Team'))
        print('{:15}{:<}'.format('','4 : Check Data Verify'))
        print('{:15}{:<}'.format('','Press x to exit Program'))
        print('{:-<50}'.format(' '))
        print("Select option")
        answer = input()
        if answer == '1':
            inputdata()
        elif answer == '2':
            dataresult()
        elif answer == '3':
            findteam()
        elif answer == '4':
            checkdata()
        elif answer == 'x':
            exit()
        else:
            print("select again")
    

