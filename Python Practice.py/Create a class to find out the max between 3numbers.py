class Max :
    a,b,c = 0 , 0 , 0
    @classmethod
    def getdata(cls) :
        cls.a,cls.b,cls.c = float(input("Enter 1st number : ")),float(input("Enter 2nd number : ")),float(input("Enter 3rd number : "))
    def max(self) : 
        max = self.a if self.a > self.b and self.a > self.c else self.b if self.b > self.a and self.b > self.c else self.c
        return max
def main() : 
    obj1 = Max() 
    Max.getdata()
    print("The  greatest of all the 3 numbers is : ",obj1.max())

if __name__ == '__main__' : 
    main()