#print('\nThis is my python file')

import sys
import csv
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import docx
#from docx2pdf import convert
from fpdf import FPDF
from datetime import datetime


if len(sys.argv) != 3:
    sys.stderr.write("Usage:./newAuto.sh filename.csv\n".format(sys.argv[0]))
    exit()
now = datetime.now()
file_name = sys.argv[1]
host = sys.argv[2]

df = pd.read_csv(file_name)
base_color = sb.color_palette()[0]

# services visuals
sb.set_style("darkgrid")
ax1 = sb.countplot(x="SERVICE", data=df, palette="Set3")
ax1.figure.savefig("service-result.png")

## ports visuals

ax2 = sb.countplot(x="PORT", data=df, palette="Set3")
ax2.figure.savefig("port-result.png")

#port_counts = df['PORT'].value_counts()
#plt.pie(port_counts, labels = port_counts.index, counterclock = False, startangle = 90, wedgeprops = {'width' : 0.4})
#plt.axis('square');
#plt.xticks(rotation=15)
##enhance
#plt.legend(loc = 6, bbox_to_anchor = (1.0, 0.5)) # legend to right of figure
#plt.xticks(rotation = 15)
#plt.title('Total Ports open right now')
#plt.xlabel('Port')
#plt.ylabel('Number of ports');
#plt.savefig("port-result.png")




#Report generation

logo_img = "logo.png"
service_img = "service-result.png"
port_img = "port-result.png"

report_message1 ="Results of analyzing IP: " + host +" computer"
report_message2 = "You have the following services open:"
report_message3 = "You have the following ports open! try to close unnecessarily ports:"

report_message4 = "Thank You for using the service..."
report_message5 = "Cyber security team."
report_message6 = "King Saud University - SEC 504 project"

report_message7 = "Current features include:"
report_message8 = "1. Collecting network data automatically"
report_message9 = "2. Analyzing the collected network data"
report_message10 = "3. Generate reports of the network status"


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',22);
pdf.set_text_color(176,224,230)

pdf.cell(200, 10, txt = report_message1,ln = 1, align = 'C')
pdf.image(logo_img, w=pdf.w/2.0, h=pdf.h/4.0,x=50)
pdf.cell(200, 10, txt = report_message6,ln = 4, align = 'C')

pdf.set_font('Arial','B',16);
pdf.set_text_color(0,76,153)
pdf.ln(10)
pdf.cell(200, 10, txt = report_message7,ln = 4, align = 'C')
pdf.cell(200, 10, txt = report_message8,ln = 4, align = 'C')
pdf.cell(200, 10, txt = report_message9,ln = 4, align = 'C')
pdf.cell(200, 10, txt = report_message10,ln = 4, align = 'C')


pdf.add_page()
pdf.set_text_color(0,76,153)
pdf.cell(200, 10, txt = report_message2,ln = 2, align = 'C')
pdf.image(service_img, w=pdf.w/2.0, h=pdf.h/4.0,x=50)
pdf.ln(0.15)
 
pdf.cell(200, 10, txt = report_message3,ln = 3, align = 'C')

pdf.image(port_img, w=pdf.w/2.0, h=pdf.h/4.0, x=50)
pdf.ln(10)

pdf.cell(200, 10, txt = report_message4,ln = 4, align = 'C')
pdf.cell(200, 10, txt = report_message5,ln = 4, align = 'C')

report_name = now+"final_report.pdf"
pdf.output("./reports/"+report_name,'F')


