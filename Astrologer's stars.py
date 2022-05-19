# Pattern Printing

def main()  : 
    print("Enter -1 for exit")
    while(1) : 
        try : 
            no = int(input("Enter the desired number : "))
            if(no == -1) : break
            choice = bool(int( input("Enter 1 for increasing order pattern and 0 for decreasing order pattern : ")))
            if(choice == True) : 
                for i in range(1,no + 1) : 
                    print(i * "*",end="")
                    print("\n")
            else : 
                for i in range(no,0,-1) : 
                    print(i * "*",end ="")
                    print("\n")
        except Exception as e : 
            print("Invalid Input.Please try again.")
            
if __name__ == "__main__" : 
    main()