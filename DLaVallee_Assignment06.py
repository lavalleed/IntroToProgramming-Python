# Title: Working with Functions, Classes and Methods Module06#
# Dev:  DLaVallee
# Date:  November 22, 2018
# ChangeLog: (Who, When, What)
#   RRoot, Sept 16, 2017, Created this script starting template
#   <DLaVallee>, 11/17/2018, Added code to complete assignment Module06
# Functions created for assignment module05 copied and reused
# Design and coded file location pointer functionality
# Added Class and Function Methods to complete functionality required
# Known bugs: Change file works on save, but the list view is not yet passing the new file path
#--------------------------------------------------
# -- Data --#
# declare 'Global' variables and constants shared  between functions ( bad design !!! )
#--------------------------------------------------
# objFile = An object that represents a text file
objFileName = "C:\_PythonClass\Assignment06\Todo.txt"
# variable to store change status of List[] in memory
int_not_saved = 0
# print line "Task and Priority Header
print_header = "Task & (Priority)"
# print line " ---- a nice separator text string ---- "
print_sep = " -------------------------------"
# strData = A row of text data from the text file
strData = ""
# dicRow = A row of data separated into elements of a dictionary {Key= 'Name', Values = 'Task','Priority'}
dicRow = {}
# lstTable = A dictionary that acts as a 'table' of dictionary rows
lstTable = []
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# -- Input/Output --#
# Initialize - Read persistent text file and display existing data (Step 1)
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)
#---------------------------------------------------#
#Classes start here
class main (object):
    """ This class contains functions necessary to initialize the data and presentation layers"""

    def _file_path():
        # Function that allows user to select their own text file directory location
        file_path = objFileName
        print ("File path pointer is set to: ", file_path)
        choice = input (" Would you like to change the  file path pointer? (y/n) - ")
        if choice == 'y':
            getfile_path = input ("Input an existing file path where the text file can be written 'C:\?\?\... - ")
            new_file_path = '{0}Todo.txt'.format (getfile_path)
            print (" Your Todo list data will now be stored at this location: - ", new_file_path)
            file_path = new_file_path

        else:
            print ('\n')

        return file_path

    def _initialize(file_path):
        path = file_path
        # When the program starts, load data from a text file called ToDo.txt
        print (' - Welcome to the Todo List -', '\n', print_sep)
        print (path, ' - is the current file path pointer!')

        objfile = open (path, "r")
        # read data from text file into dictionary {} and list [] objects
        for line in objfile:
            strData = line.split (",")  # readline() reads a line of the data into 2 elements
            dicRow = {"Task": strData[0].strip (), "Priority": strData[1].strip ()}
            lstTable.append (dicRow)
        # View the listTable containing dictionary key:value pairs
        print (_file_path ())
        print ("******* The current items in your ToDo list are: *******")
        _print_header_sep ()
        for row in lstTable:
            print (row["Task"] + ':' + "(" + row["Priority"] + ")")
        _print_sep ()

        # launch the menu
        _menu ()
        return [lstTable], path
    """   End of my Class Object """

# -- Initialization Layer Functions --#

def _file_path():
    # Function that allows user to select their own text file directory location
    file_path = objFileName
    print( "File path pointer is set to: ", file_path)
    choice = input (" Would you like to change the  file path pointer? (y/n) - ")
    if choice == 'y':
        getfile_path = input ("Input an existing file path where the text file can be written 'C:\?\?\... - ")
        new_file_path = '{0}Todo.txt'.format (getfile_path)
        print (" Your Todo list data will now be stored at this location: - ", new_file_path)
        file_path = new_file_path

    else:
        print('\n')

    return file_path

def _initialize(file_path):
    path = file_path
    # When the program starts, load data from a text file called ToDo.txt
    print (' - Welcome to the Todo List -', '\n', print_sep)
    print (path, ' - is the current file path pointer!')

    objfile = open (path, "r")
    #read data from text file into dictionary {} and list [] objects
    for line in objfile:
        strData = line.split (",")  # readline() reads a line of the data into 2 elements
        dicRow = {"Task": strData[0].strip (), "Priority": strData[1].strip ()}
        lstTable.append (dicRow)
    #View the listTable containing dictionary key:value pairs
    print(_file_path())
    print ("******* The current items in your ToDo list are: *******")
    _print_header_sep()
    for row in lstTable:
        print (row["Task"] + ':'+ "(" + row["Priority"] + ")")
    _print_sep()

    #launch the menu
    _menu()
    return [lstTable], path

# --- Presentation Layer Functions --- #
def _menu():
#Description: Provides interface for user interactions
#Parms: (menu input for selecting processing functions ( default is = 0 )
#Data Type: String for strChoice, List for Items
#Returns: Nothing
#rType: Nothing
    while (True):
        print("""
        Menu Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Change working directory
        x) Exit Program
        """)

        str_choice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()  # adding a new line
        # menu item 1
        if (str_choice.strip () == '1'):
          # call function to get list of items in lstTable[]
            _list_items()

        # Menu item 2
        # Add a new item to the list/Table
        # call function to add item to lstTable[]
        elif (str_choice.strip () == '2'):
            _add_item()

        # Menu item 3 method
        # Remove a new item to the list/Table
        elif (str_choice.strip () == '3'):
            remove_item ()

        # Menu item 4 method
        # Save tasks to the ToDo.txt file
        elif (str_choice.strip () == '4'):
            _save_item()

        # Menu item 5 method
        # Save tasks to the ToDo.txt file
        elif (str_choice.strip () == '5'):
            _file_path()

        # Menu item x method
        #  Save and Exit
        elif (str_choice.strip () == 'x'):
            _exit()
            break
# --- Processing Functions --- #
def _list_items():
    # menu item 1
    print ("- The current items in your ToDo list are: - ", '\n')
    #print(print_header & seperator)
    _print_header_sep()
    for row in lstTable:
        print (row["Task"] + "(" + row["Priority"] + ")")
    print(print_sep)


def _add_item():
    # function that loads new records into memory [] List Table
    _not_saved = '0'
    # Add item to the Multi-Dimension List of Dictionary key:value pairs
    strTask = str (input ("What is the task? - ")).strip ()
    strPriority = str (input ("What is the priority? [high|low] - ")).strip ()
    dicRow = {"Task": strTask, "Priority": strPriority}
    lstTable.append (dicRow)
    _list_items()
    return lstTable

def remove_item():
    # 5a-Allow user to indicate which row to delete
    _list_items ()
    strKeyToRemove = input ("Which TASK would you like to removed? Match the Key TEXT... - ")
    print (print_sep)
    print (strKeyToRemove)
    blnItemRemoved = False  # Creating a boolean Flag
    intRowNumber = 0
    while (intRowNumber < len (lstTable)):
        if (strKeyToRemove == str (
                list (dict (lstTable[intRowNumber]).values ())[0])):  # the values function creates a list!
            del lstTable[intRowNumber]
            blnItemRemoved = True
        # end if
        intRowNumber += 1
    # end for loop
    # 5b-Update user on the status
    if (blnItemRemoved == True):
        _not_saved = 0
        print ("The task was removed.")

    else:
        print ("Task NOT FOUND! Case and spelling sensitive. Try again . . .")

    # 5c Show the current items in the table
    print ("******* The current items in the ToDo list are: *******")
    _print_header_sep()
    for row in lstTable:
        print (row["Task"] + "(" + row["Priority"] + ")")
        continue  # to show the menu
    print (print_sep)

def _save_item():
    # 5a Show the current items in the table
    _list_items ()
    file_path = (_file_path())
    # Show the current path where file will be saved
    print("Saving to : ", file_path)

    # 5b Ask if they want save that data

    if ("" == str (input ("To save the To-Do list Hit Enter - ")).strip ().lower ()):
        print(file_path)
        objfile = open (file_path, "w")
        for dicRow in lstTable:
            objfile.write (dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objfile.close()
    else:
        input ("Data is NOT SAVED to file! Press the [Enter] key to continue . . .")

# -- Additional Presentation layer Print Functions -- #
def _print_header_sep ():
    # print line "Task and Priority Head
    header = ' - Task & (Priority) - '
    sep = '-------------------------------'
    print(header,'\n', sep)

def _print_sep():
    # print line " ---- a nice separator text string ---- "
    sep = ' -------------------------------'
    print(sep)

def _print_header():
    # print line "Task and Priority Header
    header = "- Task & (Priority -)"
    print(header)
def _exit():
    _save_item()
    print(' See you next time . . .')

# Main script process flow
# Step-1 Set a default working text file path and load data
_initialize (objFileName)
# Step #2 - initialize Data
# Step#3 - initialize presentation layer menu
# Steps #4 - #6 occur between functions based on user selections in menu
# Step #x - close open files and exit the script


