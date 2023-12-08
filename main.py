# Code here :)

import pandas as pd
import numpy as np
import matplotlib




# read in data
def readFile():
    try:
        # Open the file
        file = open("student-data.csv", "r")
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

# main function
def main():
    # Read the file
    fileContent = readFile()
    # Process the data
    studentData = fileToList(fileContent)

    # Create a dataframe
    studentDF = pd.DataFrame(studentData, columns=["School","Sex","Age","Address","Famsize","Pstatus","Medu","Fedu","Mjob","Fjob","Reason","Guardian","Traveltime","Studytime","Failures","Schoolsup","Famsup","Paid","Activities","Nursery","Higher","Internet","Romantic","Famrel","Freetime","Goout","Dalc","Walc","Health","Absences","G1","G2","G3"])


    # Delete unnecessary columns
    studentDF = studentDF.drop(["School", "Sex", "Address", "Famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "Reason", "Guardian", "Traveltime", "Failures", "Schoolsup", "Famsup", "Paid", "Activities", "Nursery", "Higher", "Internet", "Romantic", "Freetime", "Goout", "Walc"], axis=1)




    # Graph a relation with the age to avg of G1, G2, G3
    # # Convert the data to numeric
    studentDF["Age"] = pd.to_numeric(studentDF["Age"])

    # Organize the data "Health" from least to greatest
    studentDF = studentDF.sort_values(by="Health")

    #Print avg of each health group
    print(studentDF.groupby("Health")["G1"].mean())

    # Make the data frame add the avg of G1, G2, G3
    studentDF["G1"] = studentDF["G1"].astype(float)
    studentDF["G2"] = studentDF["G2"].astype(float)
    studentDF["G3"] = studentDF["G3"].astype(float)
    studentDF["Avg"] = studentDF[["G1", "G2", "G3"]].mean(axis=1)
    # matplotlib.use('Agg')
    #
    # # For each x value, find the mean of the y values and plot it
    # fig = studentDF.groupby("Health")["Avg"].mean().plot(x="Health", y="Avg", kind="bar", title="Health vs Avg").get_figure()
    # # Plot the data with each health group "1-5" being avg of the avg of G1, G2, G3
    #
    #
    #
    #
    #
    # # Save the plot
    # fig.savefig("healthVSavg.png")








# Call the main functiasdasda
main()