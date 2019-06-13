# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:18:11 2018

@author: jshen
"""
#Dallas McGroarty
#CPSC 223
#HW4
import sqlite3
		
class table:
    
	def __init__(self, tbl_name):
		self._name = tbl_name
		self._conn = None

    # create a table using the attrib names and types        
	def create(self, attib_names, attrb_types):
		self._conn = sqlite3.connect('somedata.db')
		attributes = str()
		for i in range(0, len(attib_names)):	#loop through len of attrb and append attrb types to attrb names 
			if i == len(attib_names)-1:
				attributes += attib_names[i] + ' ' + attrb_types[i]
			else:
				attributes += attib_names[i] + ' ' + attrb_types[i] + ', '
		
		self._conn.execute('create table if not exists ' + self._name + '(' + attributes + ')')
		
    # get the list of attribute names of the table 
	def getAttribNames(self):
		cursor = self._conn.execute('SELECT * FROM ' + self._name)
		col_names = cursor.description
		return col_names

    # insert a row into the table         
	def addRow(self, attib_vals):
		cur = self._conn.cursor()
		
		split_attr = attib_vals.split(',')	#split attribute for checking
		
		cur.execute('select * from ' + self._name + ' where CWID=' + split_attr[2])	#check if record  exists by using CWID as key                           
		exist = cur.fetchone() #fetchone from cursor
		
		if exist:				#return if it exists
			return
		else:					#else it doesn't exist, so insert record to table
			cur.execute('insert into ' + self._name + ' values (' + attib_vals.rstrip() + ')')
		
		
	 # returns a cursor  
	def retrieveAll(self):
		cursor = self._conn.execute('SELECT * FROM ' + self._name)
		return cursor
    
    # return a cursor pointing to the result set     
	def performAgeGroupBY(self, avg_col, grpby_col):
		cursor = self._conn.execute('select ' + grpby_col + ', Avg(' + avg_col + ') from (' + self._name + ') group by ' + grpby_col)
		return cursor
		
	#close database
	def closeDB(self):
		self._conn.commit() #commit all data inserted into database
		self._conn.close()	#close the db
