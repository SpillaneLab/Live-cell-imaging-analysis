# Live cell imaging analysis
Icy and Python scripts for analysis of live cell imaging experiments.
# Overview 
These analysis pipelines are used for processing live cell data e.g., obtaining cell area and fluorescence intensity changes over time. 
# Installation 
Analysis performed using: <br/> <br/>
•	Fiji (https://imagej.net/software/fiji/downloads) <br/> <br/>
•	Icy (https://icy.bioimageanalysis.org/download/) <br/> <br/>
•	Spyder (https://docs.spyder-ide.org/current/installation.html) <br/> <br/>
Download and install software from relevant websites. Then: <br/> <br/>
Fiji <br/> <br/>
1.Copy the code (from browser or download as .txt) and paste into macro window as: 
     Plugins > New > Macro <br/> <br/>
2.Ensure the language is set to IJ1 Macro in the Language tab of the macro window. <br/> <br/>
3.Save the macro using .ijm extension. <br/> <br/>
Icy <br/> <br/>
1.Drag the .protocol file into the Icy window to load. <br/> <br/>
Python <br/> <br/>
1.Drag .py file to Spyder to open script.
# How to use 
Flatfield and background subtract images in Fiji (Schindelin et al., 2012) prior to running analysis pipelines. Ensure correct image properties are set in Fiji and double-checked in Icy prior to running analysis. <br/> <br/>
1.	 Get cell crops <br/> <br/>
Time-courses for individual cells should be cropped and saved in .tif format. Crops should avoid other cells as can interfere with segmentation in Icy downstream. Easiest to achieve manually. <br/> <br/>
2.	 Icy_spreading_protocol.protocol <br/> <br/>
This Icy (De Chaumont et al., 2012) protocol is designed to analyze time-course images of individual cells, which should be standardized to have the cell landing frame as the first frame. The protocol segments cells based on membrane staining to get intensity (mean, max and integrated intensity, etc.) information for all channels, as well as shape descriptor (area, perimeter, roundness, etc.) information. This enables signalling (channel selected by user) and cell spreading to be monitored over time for each cell. <br/> <br/>
Image stacks are converted to a time-course series and then segmented on the cell membrane channel using thresholding defined by the user. K-means thresholding is a reliable method of segmentation, especially with variable signalling such as calcium signalling where large changes in intensity are observed over time. The number of classes for K-means thresholding can be set by the user, where K-means_3_classes.py should be run if 3 classes are set. <br/> <br/>
This protocol can also be used to do a local background subtraction for a signalling channel by running on a cropped area away from the cell of interest and performing post-processing in Excel. <br/> <br/>
Instructions for use: <br/> <br/>
1.Define the input (module 0) and output (module 18) locations. <br/> <br/>
2.Define the thresholding parameters e.g., K-means 2 classes, 3 classes or alternative thresholding method, and the channel to be thresholded.<br/> <br/>
3.Set filtering parameters to exclude any debris or poorly segmented cells. Currently set to include any segmentation greater than 1 pixel2 (0.0121 µm2). <br/> <br/>
4.Ensure the same thresholding and filtering parameters are used for different experimental conditions.<br/> <br/> 
5.Define what measurements are to be outputted (module 15) using ROI statistics. <br/> <br/>
6.Run the protocol (Icy by default will save a screenshot of the protocol and will override the previous version every time a new run is started) ensuring each module has a green tick. <br/> <br/>
7.For each cell, the following is saved: an empty folder (delete), .xlsx file with measurements, .tif file and .xml file. Opening the .tif file in Icy will load the segmentation mask, where formatting is saved in the .xml file. Every time a .tif file is opened in Icy an .xml file is automatically generated. <br/> <br/>
8.Post-processing can be performed manually in Excel or using custom Python scripts described below. <br/> <br/>
 ![Icy_spreading_protocol protocol_screenshot](https://github.com/SpillaneLab/Live-cell-imaging-analysis/assets/143707918/541c8a6a-77ba-4320-833b-a47cb8774aba) <br/> <br/>
Figure 1: Live cell spreading pipeline in Icy. <br/> <br/>
3.	K_means_3_classes.py <br/> <br/>
When using 3 classes for K-means thresholding, the default Icy output is duplicate rows for each time point. This Python script sums these rows to create a single output for each time point. Script currently set to sum area but can be changed to reference column of choice. Ensure to set input and output locations. <br/> <br/>
4.	Post_processing.py <br/> <br/>
This Python script outputs area over time for all cells (ensure all .xlsx files for cells are saved in the same folder) meaning user does not have to manually extract data. Script can be changed at line 258 to output other information over time e.g., intensity changes. Script also outputs shape descriptors at maximum cell area. Works on Excel output from Icy where there is one row per time point e.g., K-means 2 class thresholding.
# Authors 
Hannah McArthur – Icy and Python scripts and description; Archie Isted - K_means_3_classes.py script.
# References 
De Chaumont, F., Dallongeville, S., Chenouard, N., Hervé, N., Pop, S., Provoost, T., Meas-Yedid, V., Pankajakshan, P., Lecomte, T., Le Montagner, Y., Lagache, T., Dufour, A., Olivo-Marin, J.-C., 2012. Icy: an open bioimage informatics platform for extended reproducible research. Nat. Methods 9, 690–696. https://doi.org/10.1038/nmeth.2075 <br/> <br/>
Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., Preibisch, S., Rueden, C., Saalfeld, S., Schmid, B., Tinevez, J.-Y., White, D.J., Hartenstein, V., Eliceiri, K., Tomancak, P., Cardona, A., 2012. Fiji: an open-source platform for biological-image analysis. Nat. Methods 9, 676–682. https://doi.org/10.1038/nmeth.2019
