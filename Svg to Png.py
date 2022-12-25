
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


import glob
import os

print(os.getcwd())
# absolute path to search all text files inside a specific folder
path = r'C:/Users/Happy Family/Documents/New folder (2)/*.svg'
files = glob.glob(path)


s = 1
os.mkdir("Output")
for i in range(0,len(files)):
    drawing = svg2rlg(files[i])
    renderPM.drawToFile(drawing, f'Output/{s}-svgOutput.png', fmt='PNG')
    s= s+1

#    Convert  all Svg in a folder to png
