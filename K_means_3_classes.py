import numpy as np
import pandas as pd

import warnings
warnings.simplefilter("ignore")

# Location of input data - change
input_location = r"C:\Users\k19040176\OneDrive - King's College London\Methods_paper\Macros\5.Live_cell_imaging\K_means_3_classes\data.xlsx"   
# Load the data
data = pd.read_excel(input_location)
#Create array from data
data = np.array(data)   
#Get size (number of rows)
size = len(data)    

#Array to hold output data
output = np.empty((0,2), int)   

#Loop through all the rows
for i in range(size):  
    if i % 2 == 0:  # True, if the row is even. We only take every other row. 
        area = data[i, -1] + data[i+1, -1]  # Adds the area from this row and the next one. Can change column that is referenced e.g., Avg. Ch1 is -11. 
        T = data[i, 1]  # Gets the timepoint (frame)
        output = np.append(output, [[T, area]], axis=0) # Adds timepoint and final area to an array

#Set location for output csv, remember to include the name!        
output_location = r"C:\Users\k19040176\OneDrive - King's College London\Methods_paper\Macros\5.Live_cell_imaging\K_means_3_classes\Output.csv" 
#Create a CSV of the data
pd.DataFrame(output).to_csv(output_location, header=False, index=False) 

