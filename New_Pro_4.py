# ===========================================
# Project: Data Analyzer and Transformer
# ===========================================

# ---------- Global Variables ----------
data_1d = []
data_2d = []


# ---------- Function to Input 1D List ----------
def input_1d():
    #Accept 1D List from User

    global data_1d

    size = int(input("Enter the size of 1d list : "))

    data_1d = []

    print("Enter",size,"Elements : ")

    for i in range(size):
        num = int(input())
        data_1d.append(num)

    print("\n1D List Stored Successfully.")
    

# ---------- Function to Input 2D List ----------
def input_2d():
    # Accept 2D List from User

    global data_2d

    rows = int(input("Enter Size of Rows : "))
    cols = int(input("Enter Size of Columns : "))

    data_2d = []

    print("\nEnter Elements: ")
    print("Elements of [rows][columns]")
    for i in range(rows):

        row = []

        for j in range(cols):
            
            value = int(input(f"Element [{i}][{j}] : "))
            row.append(value)

        data_2d.append(row)

    print("\n2D List Stored Successfully...")


# ---------- Sample Data ----------
def sample_data():
    """Load Sample Data"""

    global data_1d
    global data_2d

    data_1d = [34,12,56,78,43,21,90]

    data_2d = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]

    print("\nSample Data Loaded Successfully!....")


# ---------- Display 1D List ----------
def display_all_data():
    """Display 1D List"""

    if len(data_1d)==0 and len(data_2d)==0:
        print("\nNo Data Available!")
        return
    
    if len(data_1d)==0:
        print("\nNo Data Available! in 1d list!")
        return

    print("\n1D List is : \n")
    print(data_1d)

    # Display 2D List in Grid

    if len(data_2d)==0:
        print("\nNo Data Available in 2D list!")
        return

    print("\n2D List is : \n")

    for row in data_2d:

        for value in row:
            print(value,end="\t")

        print()

# sort the data_1d

def sort_data():
    global data_1d
    global data_2d

    print("1. sort 1d")
    print("2. sort 2d")

    choi1=input("\nEnter your choice : ")
    if choi1=="1":

        if len(data_1d)==0:
            print("No data Avilable!")
            return

        print("\n1. Ascending")
        print("2. Descending")
    
        choi2 = (input("Enter your choice: "))
    
        if choi2 == "1":
            data_1d.sort()
            print("Sorted Data in ascending order : ", data_1d)
    
        elif choi2 == "2":
            data_1d.sort(reverse=True)
            print("Sorted Data in descending order :", data_1d)

        else:
            print("Invalid choice!")
    
    
    elif choi1 == "2":
    
        if len(data_2d) == 0:
            print("No data Available!")

        else:
            print("\n1. Ascending")
            print("2. Descending")

            choi2 = input("\nEnter your choice: ")

            if choi2 == "1":
                print("\nSorted Data in Ascending Order by rows:")
                for row in data_2d:
                    sorted1 = sorted(row)
                    print(sorted1)

            elif choi2 == "2":
                print("\nSorted Data in Descending Order by rows:")
                for row in data_2d:
                    sorted2 = sorted(row, reverse=True)
                    print(sorted2)

            else:
                print("Invalid choice!")

    else:
        print("Invalid choice!")


# 3. Recursion (Factorial)

def factorial1(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial1(n - 1)
def calculate_factorial():
    num = int(input("Enter a number to calculate factorial : "))
    if num < 0:
        print("Factorial not possible of Negative number!")
    else:
        print("Factorial of",num,"is :",factorial1(num))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def display_fibonacci():
    terms = int(input("\nEnter number to print fibonacci : "))

    print("Fibonacci Series of",terms,"number is : ")

    for i in range(terms):
        print(fibonacci(i), end=" ")

    print()


# -------------------------------
# 4. Lambda Function
# # -------------------------------
def filter_data():
    global data_1d
    global data_2d

    print("\n1. find threshold value in 1d")
    print("2. find threshold value in 2d")

    choi=input("\nEnter your choice : ")
    if choi=="1":

        if len(data_1d)==0:
            print("No data Avilable!")
            return

        threshold = int(input("Enter threshold value to greater or equal : " ))

        result = list(filter(lambda x: x >= threshold,data_1d))

        print("Filtered Data is >=",threshold,"is :",result)

    elif choi == "2":
    
        if len(data_2d) == 0:
            print("No data Available!")
            return

        threshold = int(input("\nEnter threshold value to greater or equal : "))

        # Filter all elements from the 2D list
        result = [list(filter(lambda x: x >= threshold, row)) for row in data_2d]

        print("Filtered Data (>= {}):".format(threshold))
        for row in result:
            print(row)

    else:
        print("Invalid Choice!")



# # 6. Return Multiple Values

def statistics():
    global data_1d

    if len(data_1d)==0:
        print("No data Avilable! in 1d")
        return
    lenth   = len(data_1d)
    minimum = min(data_1d)
    maximum = max(data_1d)
    total = sum(data_1d)
    average = total / len(data_1d)

#      return multiple values
    return lenth,minimum, maximum, total, average
    



def display_statistics():
    result = statistics()
    

    if result:
        lenth,minimum, maximum, total, average = result

        print("\n----- Statistics 1D-----\n")
        print("Total Elements :",lenth)
        print("Minimum :", minimum)
        print("Maximum :", maximum)
        print("Sum     :", total)
        print("Average :", average)

def dataset_summary_2d():
    global data_2d

    if len(data_2d) == 0:
        print("No data available! in 2d")
        return 

    rows = len(data_2d)
    cols = len(data_2d[0])

    flat = []
    for row in data_2d:
        flat.extend(row)

    return rows, cols, min(flat), max(flat), sum(flat)


def display_2d_statistics():
    sum=0
    result = dataset_summary_2d()

    if result:
        rows, cols, minimum, maximum, total = result
        print("\n------Statistics 2D------\n")
        sum=rows*cols
        print("all elements : ",(sum))
        print("Rows:", rows)
        print("Columns:", cols)
        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Sum:", total)

#unique values...

def unique_values():
    global data_1d
    global data_1d
    print("Unique values: ")
    if len(data_1d)==0:
        print("no data in 1d")

    else:
        convrt1=set(data_1d)
        print("unique values of 1D:",convrt1)

    if len(data_2d)==0:
        print("no data in 2d")

    else:

        print("unique values of 2D: ")
        for i in data_2d:
            cnvt=set(i)
            print(cnvt)

def average():
    global data_1d
    global data_2d
    if len(data_1d)!=0:
        avrg=sum(data_1d)/len(data_1d)
        print("\n\nAverage for 1D Elements:",avrg)

    if len(data_2d)!=0:
        print("Average for 2D Elements:")
        for i in data_2d:
            avg = sum(i) / len(i)
        print(avg)

def display_args(**args):
    """Display multiple values using *args."""

    if len(data_1d) == 0:
        print("No values found.")
        return

    print("\nValues using *args in 1d----\n")
    for key, value in args.items():
        print(f"{key}  :  {value}")


def dataset_summary(**kwargs):
    """Display dataset characteristics using **kwargs."""
    if len(kwargs) == 0:
        print("No values found.")
        return

    print("\nDataset Summary using **kwargs in 2d: \n ")

    for key, value in kwargs.items():
        print(f"{key} : {value}")
    

        



# -------------------------------
# Main Menu
# -------------------------------

print("\n==================================================")
print(" Welcome to Data Analyzer and Transformer Program")
print("====================================================")

while True:
    print("\n\nSelect An Option:")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Use Sample Data")
    print("4. Display 1D & 2D list")
    print("5. Factorial & Fibonnaci series(recursion)")
    print("6. Filter Data")
    print("7. Sort Data")
    print("8. Display Data summary")
    print("9. Display unique values and average")
    print("10.Display Dataset Statistics through *args , **kwargs")
    print("11. Exit Program!")


    choice = input("\nEnter your choice : ")

    if choice == "1":
        input_1d()

    elif choice =="2":
        input_2d()

    elif choice =="3":
        sample_data()

    elif choice == "4":
        display_all_data()

    elif choice == "5":
        # no need to call factorial1()
        calculate_factorial()
        display_fibonacci()

    elif choice == "6":
        filter_data()

    elif choice == "7":
        sort_data()

    elif choice == "8":
        display_statistics()
        display_2d_statistics()

    elif choice == "9":
        unique_values()
        average()

    elif choice=="10":
    
    
        if len(data_1d) == 0:
            print("\nNo 1D data available!")
        else:
            display_args(
                Total_elements=len(data_1d),
                Maximum_no=max(data_1d),
                Minimum_no=min(data_1d),
                Sum_of_all_ele=sum(data_1d),
                Average_is=sum(data_1d)/len(data_1d)
            )
        if len(data_2d) == 0:
            print("\nNo 2D data available!")
        else:
            dataset_summary(
                Rows=len(data_2d),
                Columns=len(data_2d[0])
            )
       

    elif choice == "11":
        print("\nThank you for using Data Analyzer and Transformer Goodbye!")
        break

    else:
        print("Invalid Choice!")