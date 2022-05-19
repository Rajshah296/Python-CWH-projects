# This program was developed by Raj Shah.
import time
from pygame import mixer
import datetime
def gettime() : 
    """This function gives time right now."""
    return datetime.datetime.now()
mixer.init()
# Here each glass of water is considered to be of 313.5 mililitres.
# So it would take the person 8 hours to drink 3.5 litres if he drinks every 43 minutes

def drink_water(): 
    """This function plays the .mp3 file,does file handling for 'Water.txt' and returns the time duration for which the function ran."""
    mixer.music.load("water.mp3")
    initial = gettime()
    mixer.music.play()
    while(1) : 
        with open("Water.txt","a") as f : 
            log = input("Type Drank only if you drank water : ").capitalize()
            if(log == "Drank") : 
                f.write(f"{log} : [{gettime()}]")
                print("Logged Successfully.")
                mixer.music.stop()
                break
            else : print("\nInvalid Input. Please enter the correct text.")

def move_eyes() : 
    """This function plays the .mp3 file and does file handling for 'Eyes.txt' and returns the time duration for which the function ran."""
    initial = gettime()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    with open("Eyes.txt","a") as f : 
        while(1) : 
            log = input("Type EyDone only if you did the eye exercises : ").capitalize()
            if(log == "EyDone") : 
                f.write(f"{log} : [{gettime()}]")
                mixer.music.stop()
                print("Logged Successfully.")
                break
            else : print("\nInvalid Input. Please enter the correct text.")

def physical_activity() : 
    """This function plays the .mp3 file and does file handling for 'Exercise.txt' and returns the time duration for which the function ran."""
    mixer.music.load("physical.mp3")
    initial = gettime()
    mixer.music.play()
    with open("Exercise.txt","a") as  f : 
        while(1) : 
            log = input("Type Exdone only if you did the workout : ").capitalize()
            if(log == "ExDone") :
                f.write(f"{log} : [{gettime()}]")
                mixer.music.stop()
                print("Logged Successfully.")
                break
            else : 
                print("\nInvalid Input. Please enter the correct text.")

def main() :  
        name = input("Enter your name : ").capitalize
        total_duration_water = 43 * 60
        total_duration_eyes = 30 * 60
        total_duration_Exercise =  45 * 60
        total_duration_Exercise2 =  datetime.datetime.minute(45)
        print("******Rules******\n\n1.Be Honest to yourself for your good.\n2.Never forget the 1st rule.")
        # Create some files if already not created.
        water_time,eyes_time,exercise_time = time.time(), time.time(),time.time()
        Begin_time = datetime.datetime() 
        End_time = datetime.datetime.hour(17) 
        while(1) : 
            if(End_time - gettime() >= total_duration_Exercise2) :
                if((time.time() - eyes_time  > total_duration_eyes)) : 
                    move_eyes()
                    eyes_time = time.time()
                elif(time.time() - water_time > total_duration_water) : 
                    drink_water()
                    water_time = time.time()
                elif(time.time() - exercise_time > total_duration_Exercise) : 
                    physical_activity()
                    exercise_time = time.time()
            else : break

if __name__ == '__main__': 
    main()