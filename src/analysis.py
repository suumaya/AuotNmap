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

#write
mydoc = docx.Document()

mydoc.add_picture(logo_img, width=docx.shared.Inches(5), height=docx.shared.Inches(7))
mydoc.add_heading(report_message1, 0)

mydoc.add_paragraph(report_message2)
mydoc.add_picture(service_img, width=docx.shared.Inches(5), height=docx.shared.Inches(7))

mydoc.add_paragraph(report_message3)
mydoc.add_picture(port_img, width=docx.shared.Inches(5), height=docx.shared.Inches(7))

mydoc.add_heading(report_message4, 1)

mydoc.save("initial_report.docx")


# Read
doc = docx.Document("initial_report.docx")
all_paras = doc.paragraphs

for para in all_paras:
    print(para.text)
    print("-------")
