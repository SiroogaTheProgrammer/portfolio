import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from tabulate import tabulate

print("------------------------------")
print("******************************")
print("------------------------------")
print("This is an IB grade calculator")
print("------------------------------")
print("******************************")
print("------------------------------")
print("\033[32mEnter 'i' for more information\033[0m")
print("------------------------------")
print("How many subjects do you have? ")

sub = input()

while sub.isdigit() == False:
    if sub == "i":
        print('''
-------------------------------------------------------------------------------------------------------
\033[31mThis calculator is not affiliated with, endorsed by, or created in collaboration with the International 
Baccalaureate Organization (IBO). The values provided by this calculator are based on independent 
algorithms and are for general reference purposes only. They may not necessarily match the official 
calculations or results provided by the IBO. For accurate and official information, please consult 
directly with the IBO or your educational institution.\033[0m
-------------------------------------------------------------------------------------------------------
To use this calculator, first enter how many courses you want to enter and calculate values for. Then 
one by one enter your grades. For correct predictions and analysis enter the values period by period. 
After each grade press enter, to enter the next grade. When the last grade was inputed, leave the 
prompt blank and press enter. The system will ask you to enter information about the next course. If 
There are no more grades and courses to enter, the program will automatically move on to calcualting 
all the values. After finishing calculating the values graphs of grade trends will pop up in the order 
they were inputed. After closing all of them, a table of values will be displayed.
-------------------------------------------------------------------------------------------------------
        ''')
    print("How many subjects do you have? ")
    sub = input()

subjects = []

names = []

for x in range(0, int(sub)):
    print("Subject " + str(x+1) + ": ")
    subject = input()
    subjects.append([subject])
    names.append(subject)
    
    key = True
    while key == True:
        print("grade: ")
        grade = input()
        if grade:
            subjects[x].append(int(grade))
        else:
            key = False

averagePerSub = []
averagePerSubRD = []
average = 0
averageRD = 0
predictedPerSub = []
points = 0
trends = []

def calculate_trend(value, average):
    values = value[1:]
    
    x = np.arange(len(values))  # Create an array of index values (time)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, values)
    
    # Calculate the regression line (y = mx + b)
    regression_line = slope * x + intercept
    
    # Plot the original values
    plt.scatter(x, values, label='Data points', color='blue')
    
    # Plot the regression line
    plt.plot(x, regression_line, label=f'Linear fit (slope={slope:.2f})', color='red')
    
    plt.xticks(np.arange(0, len(values), 1))
    
    plt.ylim(1, 7)
    
    # Labels and title
    plt.xlabel('Index')
    plt.ylabel('Grade')
    plt.title('Grade Trend for ' + value[0])
    plt.legend()

    # Display the plot
    plt.show()

    if slope > 0:
        trends.append("Upward trend")
    elif slope < 0:
        trends.append("Downward trend")
    else:
        trends.append("Stable trend")
        
    predictedPerSub.append(average + (average - int(average))*slope)
    

for subject in subjects:
    av = float(sum(subject[1:]))/float((len(subject)-1))
    averagePerSub.append(av)
    averagePerSubRD.append(math.floor(av))
    
    trend = calculate_trend(subject, av)

average = float(sum(averagePerSub))/float((len(averagePerSub)))
averageRD = math.floor(average)

headers = ["Subject", "Average", "Average Rounded Down", "Grade Trend", "Predicted"]

data = []

for x in range(0, len(names)):
    ls = []
    ls.append(names[x])
    ls.append(averagePerSub[x])
    ls.append(averagePerSubRD[x])
    ls.append(trends[x])
    ls.append(predictedPerSub[x])
    data.append(ls)


# Print the table
print(tabulate(data, headers=headers, tablefmt="pretty"))

print("Average of all grades: " + str(average))
print("Average rounded down: " + str(averageRD))
print("\033[31mIMPORTANT!\033[0m" + " IBO ROUNDS GRADES DOWN")