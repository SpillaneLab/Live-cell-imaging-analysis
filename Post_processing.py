# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:02:53 2020

@author: k19040176
"""

#Import everything you need
import pandas as pd
import matplotlib.pyplot as plt 
import os
import math
import xlsxwriter
import os.path


#Map to output directory (make sure to use forward slashes for file path)
#Read as .xlsx file as default Icy output not .csv
#Setup to read all Excel files within folder (save Icy outputs from multiple cells in the same folder)


#Create a workbook to write Python output too - make sure to name!
workbook = xlsxwriter.Workbook("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Output/Python_Output.xlsx")

#Add worksheet within workbook where shape descriptors will be added
worksheet1 = workbook.add_worksheet("Shape_des")

#Write a column with shape descriptor names
row = 1
column = 0
worksheet1.write(row, column, "Time (min)")
row = 2
column = 0
worksheet1.write(row, column, "Sphericity (%)")
row = 3
column = 0
worksheet1.write(row, column, "Roundness (%)")
row = 4
column = 0
worksheet1.write(row, column, "Convexity (%)")
row = 5
column = 0
worksheet1.write(row, column, "Elongation Ratio")
row = 6 
column = 0
worksheet1.write(row, column, "Perimeter (um)")
row = 7 
column = 0
worksheet1.write(row, column, "Area (um2)")
row = 8
column = 0
worksheet1.write(row, column, "Circularity")
           
#Create a column with file names as the heading 

#Start from the second column 
row = 0
column = 1 

#Iterate through the files in the input folder
files =[]
for i in os.listdir("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input"):
    if i.endswith('.xlsx'):
        #Get file name without extension 
        file_name_with_extension = os.path.basename(i)
        index_of_dot = file_name_with_extension.index('.')
        fileName = str(file_name_with_extension[:index_of_dot])
        
        #Write operation
        worksheet1.write(row, column, fileName)
        
        #Increment the value of the column by one for each iteration
        column += 1

#Populate the column with shape descirptors 

#Start from the first column
column = 1 

#Iterate through the files in the input folder
files =[]
for i in os.listdir("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input"):
    if i.endswith('.xlsx'):
        #Get file name without extension 
        file_name_with_extension = os.path.basename(i)
        index_of_dot = file_name_with_extension.index('.')
        fileName = str(file_name_with_extension[:index_of_dot])
        
        #Read all Excel files within input directory 
        df = pd.read_excel("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input/" + fileName + ".xlsx")
            
        #Insert column where you can convert frame number (T) to time
        #Change calculation to match interval time used for imaging
        df.insert(2, "Time (min)", True) #Insert empty column 
        df["Time (min)"] = (df["T"]*5)/60 #Populate the column with time values
        df.sort_values("Time (min)", ascending=True) #Sort into ascending order
        
        #Change area column name (because cannot read micro symbol)
        df.rename(columns={ df.columns[17]: "Area" }, inplace = True)
            
        #Change perimeter column name (because cannot read micro symbol)
        df.rename(columns={ df.columns[16]: "Perimeter" }, inplace = True)
       
        #Insert circularity column as will calculate manually
        df.insert(18, "Circularity", True)  
        
        #Calculate circularity
        #Set the value for pi
        pi = math.pi
        area_4pi = df["Area"]*4*pi
        perimeter_squared = df["Perimeter"]**2
        #Populate the column with circularity values
        df["Circularity"] = (perimeter_squared/area_4pi) 
        
        #Get shape descriptors at max cell area 
        
        #Define max cell area row
        max_area_row = df['Area'].idxmax()
       
        #Get shape descriptors
        time = float(df.at[max_area_row,'Time (min)'])
        sphericity = float(df.at[max_area_row,'Sphericity (%)']) 
        roundness = float(df.at[max_area_row,'Roudness (%)'])
        convexity = float(df.at[max_area_row,'Convexity (%)']) 
        elong_ratio = float(df.at[max_area_row,'Elongation ratio']) 
        perimeter_um = float(df.at[max_area_row,'Perimeter']) 
        area_um = float(df.at[max_area_row,'Area']) 
        circularity = float(df.at[max_area_row,'Circularity'])
        
        #Write shape descriptors 
        row = 1
        worksheet1.write(row, column, time)
        row = 2 
        worksheet1.write(row, column, sphericity)
        row = 3
        worksheet1.write(row, column, roundness)
        row = 4
        worksheet1.write(row, column, convexity)
        row = 5
        worksheet1.write(row, column, elong_ratio)
        row = 6 
        worksheet1.write(row, column, perimeter_um)
        row = 7 
        worksheet1.write(row, column, area_um)
        row = 8
        worksheet1.write(row, column, circularity)
            
        #Increment the value of the column by one for each iteration
        column +=1
                           
#Make a worksheet for time and area 
worksheet2 = workbook.add_worksheet("Time_area")

#Create a row with filenames as the heading 

#Start from the first cell
row = 0
column = 0 

#Iterate through the files
files =[] 
for i in os.listdir("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input"):
    if i.endswith('.xlsx'):
        #Get file name without extension 
        file_name_with_extension = os.path.basename(i)
        index_of_dot = file_name_with_extension.index('.')
        fileName = str(file_name_with_extension[:index_of_dot])
        
        #Write operation
        worksheet2.write(row, column, fileName)
        
        #Increment the value of the column by two for each iteration (time and area)
        column += 2
        
#Write the time for each file 

#Define the start cell
column = 0 

#Iterate through the files
files =[]
for i in os.listdir("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input"):
    if i.endswith('.xlsx'):
        #Get file name without extension 
        file_name_with_extension = os.path.basename(i)
        index_of_dot = file_name_with_extension.index('.')
        fileName = str(file_name_with_extension[:index_of_dot])
        
        #Read all Excel files within input directory 
        df = pd.read_excel("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input/" + fileName + ".xlsx")
        
        #Insert column where you can convert frame number (T) to time
        #Change calculation to match interval time used for imaging
        df.insert(2, "Time (min)", True) #Insert empty column 
        df["Time (min)"] = (df["T"]*5)/60 #Populate the column with time values
        df.sort_values("Time (min)", ascending=True) #Sort into ascending order
            
        # Change area column name (because cannot read micro symbol)
        df.rename(columns={ df.columns[17]: "Area" }, inplace = True)
        
        #Write 'Time' as a title
        #Define the row number 
        row = 1
        worksheet2.write(row, column, "Time (min)")
        
        #Define the row number
        row = 1
              
        #Iterate over the rows in the time column
        for (idx, rows) in df.iterrows():
            #Write the output on different rows
            row += 1
            time_value = float(rows.loc['Time (min)'])
            worksheet2.write(row, column, time_value)
                                  
        #Increment the value of the column by two for each iteration
        column += 2
    
#Write the area for each file 
#Can change to output what you want - row 258

#Define the start cell
column = 1 

#Iterate through the files
files =[]
for i in os.listdir("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input"):
    if i.endswith('.xlsx'):
        #Get file name without extension 
        file_name_with_extension = os.path.basename(i)
        index_of_dot = file_name_with_extension.index('.')
        fileName = str(file_name_with_extension[:index_of_dot])
        
        #Read all Excel files within input directory 
        df = pd.read_excel("C:/Users/k19040176/OneDrive - King's College London/Methods_paper/Macros/5.Live_cell_imaging/Python_post_processing/Input/" + fileName + ".xlsx")
        
        #Insert column where you can convert frame number (T) to time
        #Change calculation to match interval time used for imaging
        df.insert(2, "Time (min)", True) #Insert empty column 
        df["Time (min)"] = (df["T"]*5)/60 #Populate the column with time values
        df.sort_values("Time (min)", ascending=True) #Sort into ascending order
            
        # Change area column name (because cannot read micro symbol) 
        df.rename(columns={ df.columns[17]: "Area" }, inplace = True)
        
        #Write 'Area' as a title
        #Define the row number 
        row = 1
        worksheet2.write(row, column, "Area (um2)")
        
        #Define the row number
        row = 1
        
        #Iterate over the rows in the area column
        for (idx, rows) in df.iterrows():
            #Write the output on different rows 
            row += 1
            area_value = float(rows.loc['Area']) #Change column name here to output what you want, match formatting in the input Excel file
            worksheet2.write(row, column, area_value)
            
        #Increment the value of the column by two for each iteration
        column += 2

workbook.close()
       


      


