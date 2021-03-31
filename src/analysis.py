#print('\nThis is my python file')

import sys
import csv
import glob
import os
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from fpdf import FPDF
from datetime import datetime

def data_analysis():

    now = datetime.now()
    timenow = now.strftime("%m/%d/%Y")

    if len(sys.argv) != 3:
        sys.stderr.write("Usage:./newAuto.sh filename.csv\n".format(sys.argv[0]))
        exit()

    file_name = sys.argv[1]

    try:
        df = pd.read_csv(file_name)
    except:
        sys.stderr.write("You Don't Have Any Open Port! No Data to analyze...".format(sys.argv[0]))
        sys.stderr.write("Thank you for using the service...")
        sys.exit(2)


    host = sys.argv[2]
    base_color = sb.color_palette()[0]
    sb.set_style("darkgrid")

# services visuals
    ax1 = sb.countplot(x="SERVICE", data=df, palette="Set3")
    ax1.figure.savefig("service-result.png")
#ax1.xticks(rotation=15)

## ports visuals

    ax2 = sb.countplot(x="PORT", data=df, palette="Set3")
    ax2.figure.savefig("port-result.png")
#plt.xticks(rotation=15)
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
    pdf.set_text_color(173,216,230)

    pdf.cell(200, 10, txt = report_message1,ln = 1, align = 'C')
    pdf.image(logo_img, w=pdf.w/2.0, h=pdf.h/4.0,x=50)
    pdf.cell(200, 10, txt = report_message6,ln = 4, align = 'C')

    pdf.set_font('Arial','B',16);

    pdf.set_text_color(176,196,222)
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

    report_name = "final_report_"+timenow+".pdf"
    report_path = "./reports"
    pdf.output("final_report.pdf",'F')



def anomaly_detection():


    #change name of current to the one provided by shell/py?
    myFolder = 'csv_data'
    files = []
    results = []
#new scan
    current_file_name = sys.argv[1] #'csv_data/today_data.csv'
    current_file = pd.read_csv(current_file_name)

#results of comparasion
    results_file_name = 'results.csv'

    if not os.path.exists(myFolder):
        os.makedirs(myFolder)

#Multi csv files
    for file in glob.glob('csv_data/*.csv'):
        if file == current_file_name:
            continue;
        files.append(file)

        with open(os.path.join(os.getcwd(),file),mode='r') as myfile:
            df = pd.read_csv(myfile)
            for port in current_file['PORT']:
                if port not in df.values:
                    results.append({'PORT': port})

    results_df = pd.DataFrame(results, columns = ['PORT'])
    if len(results_df)>0:
        print('\033[93m'+"\n WARNINIG: NEW "+str(len(results_df))+" PORTS DETECTED!!"+'\033[0m')
        print(results_df)





#main

def main():
    data_analysis()
    anomaly_detection()

if __name__ == "__main__":
    main()
