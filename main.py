# Name: Aidan Connaughton ; Maria Mangiameli
# Course: COMSC.230.01
# Prof. Name: Dr. Omar X. Rivera Morales
# Assignment: Final Project
# Program Name: main.py
# Program brief description: This program will read in data from a file and create graphs and chi squared test statistics

import pandas as pd
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


# create a fucntion that calcualtes the chi squared statistic for each of the outside factors
def chisquared(studentDF,x):
    # finds expected value
    crosstab = pd.crosstab(studentDF['Avg'], studentDF[x])
    #Calculates chi squared statistic
    num = stats.chi2_contingency(crosstab)
    print(x)
    print(num)
    return num

# Create a function that creates graphs that is passed through the data frame and what you want to graph ex: "Age", "Health", "etc"
def createGraphs(studentDF, x):
    # Organize the data "x" from least to greatest
    studentDF = studentDF.sort_values(by=x)
    x_lower = x.lower()
    # Line graph
    fig = studentDF.groupby(x)["Avg"].mean().plot(x=x, y="Avg", kind="line", title=x + " vs Avg").get_figure()
    # Save the plot
    fig.savefig(x_lower + "VSavg-line.png")
    fig.clf()  # clear the figure
    # Scatter plot
    fig = studentDF.plot(x=x, y="Avg", kind="scatter", title=x + " vs Avg").get_figure()
    # Save the plot
    fig.savefig(x_lower + "VSavg-scatter.png")
    fig.clf()  # clear the figure
    print("Created graphs for " + x)

    return


# main function
def main():
    # Read the file
    fileContent = readFile()
    # Process the data
    studentData = fileToList(fileContent)

    # Create a dataframe
    studentDF = pd.DataFrame(studentData,
                             columns=["School", "Sex", "Age", "Address", "Famsize", "Pstatus", "Medu", "Fedu", "Mjob",
                                      "Fjob", "Reason", "Guardian", "Traveltime", "Studytime", "Failures", "Schoolsup",
                                      "Famsup", "Paid", "Activities", "Nursery", "Higher", "Internet", "Romantic",
                                      "Famrel", "Freetime", "Goout", "Dalc", "Walc", "Health", "Absences", "G1", "G2",
                                      "G3"])

    # Delete unnecessary columns
    studentDF = studentDF.drop(
        ["Address", "Famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "Reason", "Guardian",
         "Traveltime", "Failures", "Schoolsup", "Famsup", "Paid", "Activities", "Nursery", "Higher", "Internet",
         "Romantic", "Goout", "Walc"], axis=1)

    # Graph a relation with the age to avg of G1, G2, G3
    # # Convert the data to numeric
    studentDF["Age"] = pd.to_numeric(studentDF["Age"])
    studentDF["Health"] = pd.to_numeric(studentDF["Health"])
    studentDF["Absences"] = pd.to_numeric(studentDF["Absences"])
    studentDF["Dalc"] = pd.to_numeric(studentDF["Dalc"])
    studentDF["Freetime"] = pd.to_numeric(studentDF["Freetime"])
    studentDF["Studytime"] = pd.to_numeric(studentDF["Studytime"])
    studentDF["Famrel"] = pd.to_numeric(studentDF["Famrel"])

    # Make the data frame add the avg of G1, G2, G3
    studentDF["G1"] = studentDF["G1"].astype(float)
    studentDF["G2"] = studentDF["G2"].astype(float)
    studentDF["G3"] = studentDF["G3"].astype(float)
    studentDF["Avg"] = studentDF[["G1", "G2", "G3"]].mean(axis=1)

    # Get number of occurrences of each age
    print(studentDF["Age"].value_counts())

    # Get number of occurrences of each sex
    print(studentDF["Sex"].value_counts())

    # Get number of occurrences of each school
    print(studentDF["School"].value_counts())

    # Matplotlib
    matplotlib.use('Agg')

    # calculate chi squared test statistics
    chisquared(studentDF, "Health")
    chisquared(studentDF, "Absences")
    chisquared(studentDF, "Dalc")
    chisquared(studentDF, "Freetime")
    chisquared(studentDF, "Studytime")
    chisquared(studentDF, "Famrel")



    # Create a graph for each of the columns
    createGraphs(studentDF, "Age")
    createGraphs(studentDF, "Health")
    createGraphs(studentDF, "Absences")
    createGraphs(studentDF, "Dalc")
    createGraphs(studentDF, "Freetime")
    createGraphs(studentDF, "Studytime")
    createGraphs(studentDF, "Famrel")

    print("Done")


main()