#writing the data
file1 = open('output.txt','w')
writing_file = file1.write("Its going great")
print (writing_file)
file1.close()

#reading the data
file1=open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()

#appending the data
file1=open('output.txt','a')
appending_file = file1.write("Python learning is fun")
print(appending_file)
file1.close()

#reading the data
file1=open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
