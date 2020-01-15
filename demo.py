#! /bin/python3
#  Jan 20 (PJW)

#  Example of string concatenation

s1 = "The"
s2 = "Maxwell"
s3 = "School"

name = s1+" "+s2+" "+s3

print("Printing it to the screen:")
print(name)

#  Example of writing to a file.

#  Note that each write call has \n at the end. That adds a
#  return character; it's not needed with print, which adds it
#  automatically when writing to the screen. Print also prints
#  multiple items and adds spaces between them.

filename = "demo.txt"

fh = open(filename,"w")

fh.write("Where was this file was written?\n")
fh.write(name+"!\n")

fh.close()

print("Wrote it to",filename,"as well.")
