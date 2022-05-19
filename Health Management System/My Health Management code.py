client_list,activity_list = ["Raj","Hammad","Modi"],["Exercise","Food"]
def gettime() : 
    """This function gives time"""
    import datetime
    return datetime.datetime.now()

def log(name,activity) :
    """This function is used to log the particular activity for a particular client."""
    resume = "y"
    while resume is "y" : 
        activity_inp = input("Enter the data : ")
        with open(f"{name}.{activity}.txt","a") as f :
            f.write(f"[{gettime()}] : {activity_inp}\n")
            print("Logged successfully.\n")
        resume = input("Add more y/n : ")

def retrieve(name,activity) : 
    """This function is used to retrieve the activity-related for a particular client with the specfied timestamp."""
    with open(f"{name}.{activity}.txt") as f: 
        print(f"{name} {activity} report")
        print(f.read())
def main()  : 
    print("Enter -1 for exit.")
    while(1) : 
        try : 
            inp = int(input("Enter 1 for log and 2 for retrieve : "))
            if inp == -1 : 
                print("Thanks for using the Health Management System")
                break 
            name,activity = input("Enter the client name : "),input("Enter the activity : ")
            print("Invalid client name or activity.Please try again.") if name not in client_list or activity not in activity_list else log(name,activity) if inp == 1 else retrieve(name,activity)
        except Exception as e:
            print("Invalid Input. Please try again.") 
            
if __name__ == "__main__" : 
    main()