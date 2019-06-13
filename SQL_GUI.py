#Dallas McGroarty
#CPSC 223
#HW4
from table import *
import sqlite3
from tkinter import *

#open file containing table name, and attributes
file = open("db_input.txt", "r")

#read each line and place into list input_string
input_string = file.readlines()

file.close() #close the file after reading lines

#first line read is table_name
table_name = input_string[0]

#second line and third read is list of attributes names and type
attr_names = input_string[1]
attr_types = input_string[2]

#strip and split attribute names and types
attr_names = attr_names.strip().split(',')
attr_types = attr_types.strip().split(',')

#create student table
student_tbl = table('Student')
student_tbl.create(attr_names, attr_types)

#get attribute names from table
attributes = student_tbl.getAttribNames()

			
#insert values into database
for obj in input_string[3:len(input_string)]:
	student_tbl.addRow(obj)

#perform age group by
print('Average GPA grouped by Age:')
curr_avg = student_tbl.performAgeGroupBY('GPA', 'Age')
for obj in curr_avg:
	print(obj)

#function to output records in gui using tkinter
def printDB():
	global col_counter	#keeps track of column number
	global row_counter	#keeps track of row number
	for column in attributes:
		lbl = Label(root, text=column[0], bg='red')
		lbl.grid(row=1, column=col_counter, pady=5, padx=5)
		col_counter += 1
		
	col_counter = 0 #reset coulmn counter for records
	count = 0	#count to limit number or records listed on gui
	
	curr_all = student_tbl.retrieveAll() 
	for x in curr_all:
		if count < 20: #record limit set to 20
			x = str(x)		
			x = x.strip('(')
			x = x.strip(')')
			elem = x.strip().split(',')
			for e in elem:
				lbl = Label(root, text=e, bg='yellow')
				lbl.grid(row=row_counter, column=col_counter, pady=5, padx=5)
				col_counter += 1
			col_counter = 0 		
			row_counter += 1		
			count += 1
		
	
col_counter = 0
row_counter = 2

root = Tk()


printDB()
	
root.mainloop()

student_tbl.closeDB()	#close database