#Right-Angled Triangle Pattern in Python

rows=int(input("Enter the rows size for the pattern: "))
for i in range(1,rows+1): # Outer loop for  rows
    for j in range(1,i+1):    #inner loop for columns
        print("*", end=" ")   #print star
    print()
