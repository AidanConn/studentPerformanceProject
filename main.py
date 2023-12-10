# Code here :)

import pandas as pd
import numpy as np
import matplotlib
from scipy import stats




# read in data
def readFile():
    try:
        # Open the file
        file = open("file.txt", "r")
        # Read the file
        fileContents = file.readlines()
        # Close the file
        file.close()
        # Return the file content
        return fileContents
    except:
        print("Error reading the file")
        exit()



def fileToList(data):
    # Create a list to store the data
    cryptoData = []
    # Loop through the data and store it in the list (Skip the first line and empty lines)
    for i in range(1, len(data) - 1):
        # Split the data and store it in a list
        line = data[i].split(";")
        # Remove "\n" from the last element
        line[-1] = line[-1].strip("\n")
        line[-2] = line[-2].strip('"')
        line[-3] = line[-3].strip('"')





        # Store the data in a list
        cryptoData.append(line)
    return cryptoData


# use pandas to organize data set

# create a chart

# create a fucntion that calcualtes the chi squared statistic for each of the outside factors
def chisquaredHealth(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Health'])
    num=stats.chi2_contingency(crosstab)
    return num
def chisquaredAbsenses(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Absences'])
    num=stats.chi2_contingency(crosstab)
    return num
def chisquaredStudy(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Studytime'])
    num=stats.chi2_contingency(crosstab)
    return num
def chisquaredFamrel(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Famrel'])
    num=stats.chi2_contingency(crosstab)
    return num
def chisquaredAlc(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Dalc'])
    num=stats.chi2_contingency(crosstab)
    return num
def chisquaredFree(studentDF):
    crosstab=pd.crosstab(studentDF['Avg'],studentDF['Freetime'])
    num=stats.chi2_contingency(crosstab)
    return num
# main function
def main():
    # Read the file
    fileContent = readFile()
    # Process the data
    studentData = fileToList(fileContent)

    # Create a dataframe
    studentDF = pd.DataFrame(studentData, columns=["School","Sex","Age","Address","Famsize","Pstatus","Medu","Fedu","Mjob","Fjob","Reason","Guardian","Traveltime","Studytime","Failures","Schoolsup","Famsup","Paid","Activities","Nursery","Higher","Internet","Romantic","Famrel","Freetime","Goout","Dalc","Walc","Health","Absences","G1","G2","G3"])


    # Delete unnecessary columns
    studentDF = studentDF.drop(["School", "Sex", "Address", "Famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "Reason", "Guardian", "Traveltime", "Failures", "Schoolsup", "Famsup", "Paid", "Activities", "Nursery", "Higher", "Internet", "Romantic", "Goout", "Walc"], axis=1)




    # Graph a relation with the age to avg of G1, G2, G3
    # # Convert the data to numeric
    studentDF["Age"] = pd.to_numeric(studentDF["Age"])
    studentDF["Health"] = pd.to_numeric(studentDF["Health"])


    # Organize the data "Health" from least to greatest
    studentDF = studentDF.sort_values(by="Health") # THis does not work



    # Make the data frame add the avg of G1, G2, G3
    studentDF["G1"] = studentDF["G1"].astype(float)
    studentDF["G2"] = studentDF["G2"].astype(float)
    studentDF["G3"] = studentDF["G3"].astype(float)
    studentDF["Avg"] = studentDF[["G1", "G2", "G3"]].mean(axis=1)

    # Print the mean of the Health for each number ("1", "2", "3", etc)

    print(studentDF.groupby("Health")["Avg"].mean())

    matplotlib.use('Agg')
    #calculate chi squared test statistics
    # calculating health x^2
    health = chisquaredHealth(studentDF)
    print("health\n")
    print(health)

    # calculating health x^2
    absenses = chisquaredAbsenses(studentDF)
    print("absenses\n")
    print(absenses)

    # calculating study time x^2
    study = chisquaredStudy(studentDF)
    print("study\n")
    print(study)

    # calculating family relations x^2
    famrel = chisquaredFamRel(studentDF)
    print("famrel\n")
    print(famrel)

    # calculating daily alcohol consumption x^2
    dalc = chisquaredAlc(studentDF)
    print("dalc\n")
    print(dalc)

    # calculating free time x^2
    free = chisquaredFree(studentDF)
    print("free\n")
    print(free)

    #What are the types of graphs that can be used?
    # Scatter plot
    # Bar graph
    # Pie chart
    # Histogram
    # Box plot
    # Area plot
    # Scatter plot

    # For each x value, find the mean of the y values and plot it
    #fig = studentDF.groupby("Health")["Avg"].mean().plot(x="Health", y="Avg", kind="line", title="Health vs Avg").get_figure()


    #fig = studentDF.plot(x="Health", y="Avg", kind="scatter", title="Health vs Avg").get_figure()


    # Save the plot
    #fig.savefig("healthVSavg-scatter.png")

main()

