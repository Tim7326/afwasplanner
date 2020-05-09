from datetime import date, timedelta
import datetime
import calendar
from names import Name
import random


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

def initialize_names():
    names=[
    Name("Tim" , 0),
    Name("Eva" , 0),
    Name("Nina" , 0),
    ]
    return names


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

def plan_week(names):
    #coming_week = bool(input("Wil je de planning voor komende week maken? 1/0"))
    #if coming_week==True:
        weeknr = date.today().isocalendar()[1]
        print(weeknr)
        dates = days_in_week(weeknr)
        for day in dates:
            day_of_week = int(day.weekday())
            print(day_of_week)
            if day_of_week==4:
                print("Op vrijdag doen papa en mama de afwas!" + str(day_of_week))
            else:
                possibilities=[]
                for x in range(len(names)): #Maak possibilities aan de hand van alle namen in initialize_names
                    possibilities.append(names[x].name)
                
                removes=[]
                for name in possibilities: #Namen die niet kunnen toevoegen aan Removes
                    if check_exception(name, day_of_week)==True:
                        print(name +" kan niet op " + str(day_of_week))
                        removes.append(name)
                for name in removes: #Namen in removes weghalen uit de dag
                    possibilities.remove(name)
                print(possibilities) 
                aan_de_beurt = random.choice(possibilities)
                print(aan_de_beurt + " is aan de beurt!")

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
                        




def add_to_archive(weeknr):
    print("test")

def show_schedule():
    print("Test")


names = initialize_names()
plan_week(names)