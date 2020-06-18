# Opening a file by open()
a = open("new.txt","w")

# w is for opening the file to write
# creates the file if it doesn't exists

# Method to write a multiline or single string:
a.write("""Another new line from Python!
Hello World!
""")
a.close() #closing the file

b = open("new.txt")
print(b.read()) 