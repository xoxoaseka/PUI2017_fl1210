# PUI2017 HW 2

Homework was done individually.


# Assignment 1:  tracking each vehicle for a line

Check how many arguments are passed to python.

Get the MTA key and bus line information from sys.argv list.

Use the MTA key to download data from MTA.

Read the data and print out the name, number and location of all available buses for the bus line from the input argument.


# Assignment 2: next stop information

First 3 steps are similar to assignment 1.

Read the data and use the json.loads method to obtain a dictionary of data.

Check if the OnwardCalls field is empty. If the there is no information, put "N/A" as values for bus stops and status.

Write the output (bus location, stop name and status) to a CSV file named by the input argument.


# Assignment 3: Read CSV files with pandas

Check if the environmental variable DFDATA exists.

Read in the CSV file from the DF into a pandas dataframe.

Remove all but 2 numerical values columns which is the infromation of X and Y coordinates of location of refuse and recycling disposal networks for each community district.

Plot a scatter plot of location of refuse and recycling disposal networks.

# Extra Credit Assignment : work with dates in Pandas

Check if the environmental variable DFDATA exists.

Read in the CSV file from the DF into a pandas dataframe. Change ['Date'] into datatime format.

Remove all but a date/time column and a numerical value.

Plot average 24hr turbidity changes of water from 2015 to 2017.

