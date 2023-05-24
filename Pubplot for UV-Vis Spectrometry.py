#Import Libraries
import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

print(' \n Welcome to PubPlot-for-UV-Vis-Spectrophotmetry by Rizwann234 ')
print('--------------------------------------------------------------')
print('\nInitialising plot settings ...')

font = input('\nPlease select a font : ')
lw = float(input('Select linewidth : '))

mpl.rcParams['font.family'] = font
mpl.rcParams['lines.linewidth'] = lw

#Specifying filepaths

def filepath_compiler() :
    
    file_count = int(input('\nHow many spectra are you trying to plot on one graph : ')) 

    count = 0
    spectra = []

    while count < file_count :
    
        fp = input(f'\nspecify the file path of spectrum ({count + 1}) \n File path : ')
        spectrum_i = fp.replace(" \ ", "/" )
        spectra.append(spectrum_i)
        count += 1
#        
        if count > file_count :
            break
    
    return spectra

# Confirming the users selections

spectra = filepath_compiler()
print('\nLoaded files : ')
[print(spectrum) for spectrum in spectra]

# Converting the specified filepaths into DataFrames. 

def file_loader(spectra) :

    data = []

    for s in spectra :

        data_i = pd.read_csv(s)
        data.append(data_i)

    return data

compiled_data = file_loader(spectra)

#Plotting spectra from each dataframe onto one graph.

def autoplotter(compiled_data) :

    print('\nsetting axis boundaries ...')
    
    user_string = input('please input 4 numbers separated by a single space i.e. X_MIN X_MAX Y_MIN Y_MAX : ')
    params = user_string.split()
    for j in range(len(params)) :
        params[j] = int(params[j])

    x_min, x_max , y_min, y_max = params[0], params[1], params[2], params[3]


    for i in range(0, len(compiled_data)) :
        input_i = compiled_data[i]
        label_i = input('\nPlease enter label name : ')
        color_i = input('Please enter colour : ')
        
        plt.plot(input_i.iloc[:,0], input_i.iloc[:,1], 
                label = label_i,
                linewidth = 1,
                color = color_i)
        
    plt.xlabel('Wavelength (nm)', fontname = font)
    plt.ylabel('Absorbance (a.u.)', fontname = font)
    plt.xlim(left = x_min , right = x_max)
    plt.ylim(bottom = y_min, top = y_max)
    plt.legend()

    directory = input('\nEnter file destination : ')
    filename = input('Filename : ')
    fmt = input("Format (png, pdf, svg, jpg) : ")
    
    img = f"{directory}\{filename}.{fmt}"
    
    plt.savefig(img.replace(" \ ", "/" ), bbox_inches = "tight")

autoplotter(compiled_data)