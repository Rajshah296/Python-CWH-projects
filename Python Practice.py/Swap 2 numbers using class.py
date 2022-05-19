class swap_num : 
    a,b = 0,0
    @classmethod
    def getdata(cls) : 
        cls.a,cls.b = int(input("Enter 1st number : ")),int(input("Enter 2nd number : ")) 
    @classmethod
    def swap(cls) : 
        cls.a,cls.b = cls.b,cls.a
    @classmethod
    def output(cls) : 
        print("\nThe 1st number is : ",cls.a,"\nThe 2nd number is : ",cls.b)

def main() :
    first_swap = swap_num()
    first_swap.getdata()
    first_swap.swap()
    first_swap.output()

if __name__ == '__main__' : 
    main()