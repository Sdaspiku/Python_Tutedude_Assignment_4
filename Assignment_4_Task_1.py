n = input('Enter the file name')

try:

    file1=open(n,'r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except:
    print("File ", n, "not found. Please check the file name.")
    
    
