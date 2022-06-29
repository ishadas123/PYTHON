
    n = int(input("Enter Number :"))
    if(n%2!=0 or (5<n<21 and n%2==0)):
        print("Weird")
    if ((n%2==0 and n>20) or (n%2==0 and 1<n<6)):
        print("Not Weird")
        
