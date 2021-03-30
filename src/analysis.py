print('\nThis is my python file')

import sys
import csv
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    sys.stderr.write("Usage:./newAuto.sh filename.csv\n".format(sys.argv[0]))
    exit()

file_name = sys.argv[1]
df = pd.read_csv(file_name)
base_color = sb.color_palette()[0]

#visuals
#print(df.head())

#Plt.figure()
sb.set_style("darkgrid")

#port visuals
ax1 = sb.countplot(x="SERVICE", data=df, palette="Set3")
ax1.figure.savefig("service-result.png")

#Port visuals
ax1 = sb.countplot(x="PORT", data=df, palette="Set3")
ax1.figure.savefig("port-result.png")

#Report generation

