# Example file for Advanced Python by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint
import collections


# regular assignment statements assign a value
max_size = 5
print(max_size)

# the assignment operator is part of an expression

# The assignment expression is useful for writing concise code
myStr = "none"

# What the loop condition would normally look like
#while ( myStr != "exit" ) :
#    myStr = input("Get Value: " )

# The walrus operator can help reduce redundant function calls
while ( (myStr := input("Get Value: ")) != "exit" ) :
    print("    still going: ", myStr)

#define my list of Val_Data objects
data = []

x = 1
while x < max_size :
    data.append( {
        "name": ("test" + str(x)),
        "length": x,
        "total": (x * 10)    
            } )
    x += 1

print("Standard print call (prints with , sep): ")
print( data )

print("Special print call (prints with NO sep): ")
print( *data )

print("Special print call using custom separator: ")
print( *data, sep=" -- " )

print("Printed using for loop: ")
for item in data:
    print( item, end=" --> End of record\n" )

# print to a file
print("Special print call to a file; flushing immediately: ")

""""
When opening a file in text mode in Python, you can use the following modes:
   'r': Read mode (default). Opens the file for reading only.
   'w': Write mode. Opens the file for writing, creating it if it doesn't exist, and truncating it if it does.
   'a': Append mode. Opens the file for writing, creating it if it doesn't exist, and appending to the end of the file if it does.
   'r+': Read and write mode. Opens the file for both reading and writing.
   'w+': Write and read mode. Opens the file for both writing and reading, truncating it if it exists, and creating it if it doesn't.
   'a+': Append and read mode. Opens the file for both appending and reading, creating it if it doesn't exist.
""" 
testFile = open("testFile.txt", "w+")

# NOTE: last record won't get separator until you add to END text
print( *data, file=testFile, sep=" -- \n", end=" -- \nEND OF RECORDS\n", flush=True )
#print( data, file=testFile, flush=True )

