from datetime import date, timedelta
import datetime
import calendar
from names import Name
import random
import os

def insert_exceptions():
    print("Test")
    #Vragen van wie de uitzondering is

    #Vragen of de uitzondering eenmalig is

    #Vragen welke dag van de week de uitzondering is

def check_exception(name, day_of_week):
    print(name)
    exceptions=[
        
        ["Tim"],
        ["Tim", "Eva"],
        ["Nina", "Eva"],
        [""],
        ["Tim"],
        ["Eva", "Nina"],
        [""] 
        
    ]
    if name in exceptions[day_of_week]:
        print(name + " kan niet op "+str(day_of_week))
        return True
    else:
        return False

def initialize():
    names=[
    Name("Tim" , 0),
    Name("Eva" , 0),
    Name("Nina" , 0),
    ]
    datalist=[]
    return names, datalist


def days_in_week(WEEK):
    iso_d = str(date.today().year) + "-W"+str(WEEK)
    print(iso_d)
    r=datetime.datetime.strptime(iso_d+'-1',"%Y-W%W-%w")
    print(r)
    week_dates=[]
    for i in range(7):
        day=r+timedelta(days=i)
        week_dates.append(day)
    print(week_dates)
    return week_dates

def plan_week(names, datalist, weeknr):
    #coming_week = bool(input("Wil je de planning voor komende week maken? 1/0"))
    #if coming_week==True:
        
        dates = days_in_week(weeknr)
        for day in dates:
            day_of_week = int(day.weekday())
            print(day_of_week)
            if day_of_week==4:
                print("Op vrijdag doen papa en mama de afwas!" + str(day_of_week))
                day_write(day, "Papa/Mama", datalist)
            else:
                possibilities=[]
                scores=[]
                for x in range(len(names)): #Maak possibilities aan de hand van alle namen in initialize_names
                    possibilities.append(names[x].name)
                
                removes=[]
                for name in possibilities: #Namen die niet kunnen toevoegen aan Removes
                    if check_exception(name, day_of_week)==True:
                        print(name +" kan niet op " + str(day_of_week))
                        removes.append(name)
                    else:
                        x=0 
                        for i in range(len(datalist)):
                            if name in datalist[i]:
                                x=x+1
                        print(name + " is al " + str(x)+ " keer aan de beurt geweest.")
                        scores.append(x)
                        print(scores)
                for name in removes: #Namen in removes weghalen uit de dag
                    possibilities.remove(name)
                print(possibilities)
                for name in possibilities:
                    print(name + str(scores[possibilities.index(name)]))
                
                try:
                    print(min(scores))
                    y=min(scores)
                except ValueError:
                    print("No inputs yet")
                    y=99
                for x in scores:
                    if x>y:
                        possibilities.pop(scores.index(x))
                        scores.remove(x)

                aan_de_beurt = random.choice(possibilities)
                print(aan_de_beurt + " is aan de beurt!")
                day_write(day, aan_de_beurt, datalist)

                '''
                print(possibilities)
                name = possibilities[i]
                print(name)
                print(day_of_week)
                remove_name = check_exception(name, day_of_week)
                if remove_name == True:
                    print("Pop!")
                    possibilities.pop(possibilities.index(name))
                '''
                        


def day_write(dag, persoon, datalist):
    print(dag)
    print(persoon)
    
    insert =[dag, persoon]
    datalist.append(insert)
    print(datalist)
    input()

def file_write(datalist, weeknr):
    print(datalist)
    datenow = datetime.datetime.now()
    path = os.getcwd() + "\\Afwasplanner\\"
    print(path)
    schedule_file = open(path + "log from " + datenow.strftime("%Y-%m-%d %H-%M-%S") + " made for week: " + str(weeknr)+".log", "w")
    for i in datalist:
        schedule_file.write("day: " + str(i[0].strftime("%Y-%m-%d"))+ " name: " + i[1]+"\n" )
    schedule_file.close
    




def add_to_archive(weeknr):
    print("test")

def show_schedule():
    print("Test")


names, datalist = initialize()



plan_komende_week = True
if plan_komende_week == True:
    weeknr = date.today().isocalendar()[1]
    print(weeknr)
else:
    weeknr = input("Van welke week wil je de planning maken?")
plan_week(names, datalist, weeknr)

file_write(datalist, weeknr)
#datalist = [
#   [dag, persoon]
# ]