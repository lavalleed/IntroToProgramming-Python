# Title: Working with Dictionaries#
# Dev:  DLaVallee
# Date:  November 12, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <DLaVallee>, 11/17/2018, Added code to complete assignment 5#
# Known bugs: List creation key to value pair is showing additional ':'?

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Key= 'Name', Values = 'Task','Priority'}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# Initialize - Read persistent text file and display existing data (Step 1)
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#Open the text file to make sure it is there before rest of script runs
objfile = open ("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "a+")

# -- Processing --#
# Step 1
# When the program starts, load data from
# a text file called ToDo.txt # First step is to open the text file and load data into a List and Dictionary objects
objfile = open("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "r")
def LoadFileList():
# create a list and dictionary object to store the text data being read from the text file
    try:
        list_todo = []
        objfile = open("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "r")
        #print (objfile.read ()) remove comment tag to check to see what is in the raw file
        #load text into list object
        list_todo = objfile.read().splitlines()
        print(list_todo)
        #load text into dictionary object
        objfile.close()
    except IOError:
        print("Text File Could not be Opened!")

def LoadFileDict():
    # create a list and dictionary object to store the text data being read from the text file
    try:
        dict_todo = {}
        objfile = open ("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "r")
        # print (objfile.read ()) remove comment tag to check to see what is in the raw file
        # load text into dictionary object
        for row in objfile:
            row.lstrip ()
            x = row.rstrip ('\n').split (',')
            a = x[0]
            b = x[1]
            c = x[2]
            s = ","
            dict_todo[a] = b + s + c
        print(dict_todo)
        objfile.close ()
    except IOError:
        print("Text File Could not be Opened!")

def AddItem():
    # open and read text file. Add item to the Multi-Dimension List of Dictionary key:value pairs
    try:
        add_todo = []
        objfile = open("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "r")
        # print (obj_file.read ()) remove comment tag to check to see what is in the raw file
        # load text into list object
        add_todo = objfile.read().splitlines()
        print(add_todo)
        while (True):
            int_kid = int(input("Enter a Unique Key Integer to add into the Dictionary range index: "))
            print(" This will be your new unique key index number = ", int_kid)
            str_value1 = str(input("Enter Task description: "))
            str_value2 = str(input("Enter Priority: "))
            print("I will insert KID #: ", int_kid, " Description: ", str_value1,
              " Priority: ", str_value2,'\n')
            #save to dictionary for possible future manipulation
            dicNewRow = {"KID":int_kid, "Task":str_value1, "Priority":str_value2}
            strCommit = "no"  # set to no to validate user wants to take the action
            strCommit = str(input("Do you want to make this change in the Dictionary? yes or no : "))
            if (strCommit.strip () == 'yes'):
                print(" This a a preview of your new dictionary row: ", dicNewRow)
                add_todo.append(dicNewRow)
                print(" Memory segment containing original dictionary was updated! : ", add_todo)
            strWrite = str(input("Do you want to store this change in the text file? yes or no : "))
            if (strWrite.strip () == 'yes'):
                print("Writing all edits to text file: ", add_todo)
                objfile = open("C:\\_PythonClass\\assignment05\\module05\\ToDo.txt", "w")
                objfile.write(str(add_todo))
                print(" New key:value pairs added! : ", add_todo)
                break

            else:
                print(" Nothing changed!")

        objfile.close()

    except IOError:
        print("Text File Could not be Opened!")

#Display current list of Key:Value Pairs
print('\n',"The text file contains the following Key:Value pairs . . .","\n")
print(objfile.read())

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

objFileName = "C:\_PythonClass\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add each file "row" to a python list "table"
#Display the current List object contents
#print(objfile)

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line for console output spacing

    # Step 3 -Show the current items in the table
    if (strChoice.strip () == '1'):
        print("Below is your List and Dictionary objects showing Key:Value pairs {'Key':'Value1','Value2'}")
        LoadFileList()
        LoadFileDict()
        print("Above is a Multi-Dimension Table including unique Dictionary rows of Key,Value pairs!")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip () == '2'):
        print('You selected to add a new Dictionary Row to the larger Multi-Dimension List!')
        AddItem()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        print ('Not implemented...')
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        print('Not implemented...')
        continue
    elif (strChoice == '5'):
        objfile.close()
        print ('See You Next Time...')
        break  # stop any loops and final exit the program
