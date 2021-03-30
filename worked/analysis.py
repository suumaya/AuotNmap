print('this is my python file')

import sys
import csv
import pandas as pd
import numpy as np
#import seaborn as sb

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



if len(sys.argv) != 2:
    sys.stderr.write("Usage:./newAuto.sh filename.csv\n".format(sys.argv[0]))

file_name = sys.argv[1] 
df = pd.read_csv(file_name)

#visuals
print(df.head())

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3])
fig.savefig('port-test.png')

plt.hist(df['SERVICE']);


