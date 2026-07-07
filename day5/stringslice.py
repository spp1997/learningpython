#String Slicing

#You can return a range of characters by using the slice syntax
#Specify the start index and the end index , seperated by a colon, to return a part of the string

b= "Hello, World!"
print(b[2:5])

#Slice from the start 
#By leaving out the start index, the range will start at the first character

b= "Hello, World!"
print(b[:5])


#Slice to the End
#By leaving out the end index, the range will go to the end

b= "Hello, World!"
print(b[2:])

#Negative indexing 
#Use negative indexes to start the slice from the end of the string

b= "Hello, World!"
print(b[-5:-2])


