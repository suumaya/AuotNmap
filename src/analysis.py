print('\nThis is my python file')

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

logo_img = "logo.png"
service_img = "service-result.png"
port_img = "port-result.png"

report_message1 ="Results of analyzing (this IP) network computer\n"
report_message2 = "\nServices are:\n"
report_message3 = "Ports are:\n"
report_message4 = "Cyber security team.\nSEC 504 project\nKing Saud University\n"

#convert to final_report.pdf

# write in docx, kali not support ms but worked 
#mydoc = docx.Document()
#
#mydoc.add_picture(logo_img)
#mydoc.add_heading(report_message1, 0)
#
#mydoc.add_paragraph(report_message2)
#mydoc.add_picture(service_img)
#
#mydoc.add_paragraph(report_message3)
#mydoc.add_picture(port_img)
#
#mydoc.add_heading(report_message4, 1)
#
#mydoc.save("initial_report.docx")


# convert
#convert("initial_report.docx", "final_report.pdf")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = report_message1,
         ln = 1, align = 'C')
    
pdf.cell(200, 10, txt = report_message2,
         ln = 2, align = 'C')
         
pdf.cell(200, 10, txt = report_message3,
         ln = 3, align = 'C')

pdf.cell(200, 10, txt = report_message4,
         ln = 4, align = 'C')

pdf.output("final_report.pdf")
