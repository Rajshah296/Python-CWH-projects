from asyncore import write
import datetime as dt
import os
from posixpath import split 
def gettime() : 
    """This function gives time right now."""
    return dt.datetime.now()

class Library:
    book_record = {}
    member_details = {}
    rule_list = []

# You need a dictionary for intitializing a object of Library class with the book details or you can just initialize a Library and add the books later using add_books function.
    def __init__(self,*books):
        with open("books.csv","a") as f : 
            write(split(books,","))
        self.Lib_name = input("Enter the name of the Library: ")
        
    def Rules_Management(self) : 
        try : 
            choice = input("\nChoose what you want to do : \n\n1. Add a rule\n2. Delete a rule by rule no.\n3. Type the rule you want to delete")
            self.rule_list.append(input("Enter the rule : ")) if choice == 1 else self.rule_list.pop(input("Enter the rule no. : ")) if choice == 2 else        self.rule_list.remove(input("Enter the rule you want to delete"))
        except :
            print("Oops! Something went wrong, we are trying to fix it. Stay tuned.")

    def get_rules(self) : 
        print("\nStrictly follow the rules of Library : ")
        for value,i in self.rule_list : 
            print(f"\n{i+1}. {value}")


    def show_books(self) : # This function is for admin.

        """This function shows the books Library maintains."""
        try : 
            if self.book_details == {} :
                print("\nThere are no books in Library. Please add some books first.")
            else :
                for key,value in self.book_details :
                    print(f"{key} : {value},\n")
        except :
            print("Oops! Something went wrong, we are trying to fix it. Stay tuned.")

    def add_books(self) : # This function is for admin.
        """This function adds the books in the library."""
        try :  
            self.book_details[input("\nEnter the book name : ").capitalize()] = {"Author name" : input("\nEnter the author name").capitalize(),"Price" : int(input("\nEnter the price of book")), "Length" : int(input("\nEnter the length of the book : ")), "Probable Readers" :input("\nWho are the probable readers").capitalize(), "Available copies" : int(input("\nAvailable copies : ")).capitalize()}

            print("Congrats Comrade, The book has been added.")
            result = input("\nPress y to add more and n to exit.")
            Library.add_books(self) if result == 'y' else 0  
        except :
            print("Oops! Something went wrong, we are trying to fix it. Stay tuned.")

    def lend_book(self,book_name,duration,person) : # This function is for admin.
        """This function is used to lend the book to a member or a non-member client."""
        try : 
            if book_name in self.book_details.keys() and self.book_details[book_name]["Available copies"] > 2 :
                self.book_details[book_name]["Available copies"] -= 1

                print(f"\nCongrats {person},Your lend request for {book_name} has been granted.")
        except :
            print("Oops! Something went wrong, we are trying to fix it. Stay tuned.")

    def return_book() : # This function is for User.
        """This function is used when a client returns the book."""
        pass
        
def main() : 
    print("Hi, this system was developed by Raj Shah.")
    pass
if __name__ == 'main' : 
    main()