# PubPlot-for-UV-Vis-Spectrophotmetry
Automated UV-Visible Absorbance Spectra plotting.

## Section 1 - Motivation

During my time as an undergraduate and then postgraduate student, I hated plotting and formatting graphs in excel. Alas my interest in programming came after doing a masters in chemistry. 

The motivation of this project thus came from what I wished I could haved automated during my time as a university student. The pedantic nature of academia means that your graphs have to be on point and therefore one could spend a good few minutes plotting and formatting your graphs. Therefore the objective of this program is to automate this process by simply speicfying the filepaths and plot parameters.

If you happen to come accross this repository, feel free to download the code. Any constructive feedback on the code and the user experience would be much
appreciated.

## Section 2 - Pre-requisites

Before using this code, it would be beneficial to have these downloaded if not already.

- Python, it is often better to install directly from the python website.  
  https://www.python.org/downloads/
- Dependencies : pandas, numpy, matplotlib

If you do not have these already, copy and paste these lines into your command line.

python -m pip install -U matplotlib  
python -m pip install -U pandas  
python -m pip install -U numpy  


## Section 3 - Instructions for use

**Step 1** : Open the software with the following line - python "[filepath of the python code you have saved.]"
         alternatively you can write "python"  then drag and drop the .py file into the command line.  
         ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/df455363-3858-43dc-9552-37f7a67d0ea8)  
         
           
**Step 2** : The software is now open. Proceed to specifying the font and linewidths for your plot.
            ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/2c95f8ba-d344-414f-aaae-3721638ed6fb)
            
              
**Step 3** : Select the number of curves(spectra) you would like on one plot and specify the files paths for each.  
             Again you can drag your file into the command line. Make sure these are **NOT** enclosed in quotation marks.
             After loading the files, the files you have uploaded will be listed to you. 
             ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/0f01423d-9af3-4205-bb4d-1a93cb097883)
             
**Step 4** : Now we will look into formatting axes of our plots. First define the axes paramaters of your choosing it should be in this format X_MIN X_MAX Y_MIN Y_MAX.  
             Each number should be an integer separated by a space.
             ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/808ab8bf-f54d-44a7-aa4d-ed11670b73c1)

**Step 5** : Now we will assign label names and associated colours to each spectrum. For each file, you will be asked to give a label name and colour.  
             For label colours please see the matplotlib documentation for options : https://matplotlib.org/stable/gallery/color/named_colors.html
             ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/3e834dbe-3d5a-4e93-bb05-c0f4802db633)

**Step 5** : The last step will be to save your beautiful plot. To do this, you will be sequentially prompted to specify the save directory, filename and file format.
             ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/176c4acb-ff5a-406d-8ff2-3cb366aff874)
             Following this your saved file will appear in the specified folder.
             ![image](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/cb1e2a97-adad-420f-b3f3-2ac43060a60e)

**Step 6** : You are now left with a plot of all your spectra. Congratulations!  
             ![Tutorial plot](https://github.com/Rizwann234/PubPlot-for-UV-Vis-Spectrophotmetry/assets/95040993/e56098e9-a869-4d7a-b03f-29f77057aa66)

             
 
 
