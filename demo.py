#! /bin/python3
#  Jan 20 (PJW)

#
#  Example of string concatenation
#

s1 = "The"
s2 = "Maxwell"
s3 = "School"

name = s1+" "+s2+" "+s3

print("Printing it to the screen:")
print(name)

#
#  Concatenating strings vs adding numbers
#

s20 = '20'
s21 = '21'
year = s20+s21

print( year )

n20 = 20
n21 = 21
total = n20+n21

print( total )

#
#  Writing to a file.
#

#  What should the name of the file be?

filename = "demo.txt"

#  Open a file handle for writing to the new file

fh = open(filename,"w")

#  Use the write() method to write two lines. Note that
#  write() only writes strings, and writes exactly what 
#  it's given. As a result we need to add a return 
#  character, \n, at the end of each line.

fh.write("Where was this file was written?\n")
fh.write(name+"!\n")

#  Use the print() function to write two different lines.
#
#  Print can write multiple items at once and automatically
#  formats them by: (1) converting them to strings, (2)
#  inserting spaces between them, and (3) adding a return.
#
#  The file handle goes at the end of the call.

print("It was written during",year,file=fh)
print("The answer is",total+1,file=fh)
#  Close the file

fh.close()

#  All done

print("Wrote a message to",filename,"as well.")
