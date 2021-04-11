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
from matplotlib.pyplot import step, show
from fpdf import FPDF
from datetime import datetime


dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path+"/csv_data/"+sys.argv[1]
host = sys.argv[2]
base_color = sb.color_palette()[0]

def data_analysis():

    now = datetime.now()
    timenow = now.strftime("%d/%m/%Y")
    if len(sys.argv) != 3:
        sys.stderr.write("Usage:./newAuto.sh filename.csv\n".format(sys.argv[0]))
        exit()


    try:
        df = pd.read_csv(file_name)
    except:
        sys.stderr.write("You Don't Have Any Open Port! No Data to analyze...".format(sys.argv[0]))
        sys.stderr.write("Thank you for using the service...")
        sys.exit(2)


   
    
    sb.set_style("darkgrid")
    df_of_open_ports = df.loc[lambda df: df['STATE'] == "open"]
   
   
    # services visuals
    ax = sb.countplot(x="SERVICE", data=df,palette="Set2")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.figure.savefig("/home/kali/Desktop/src/photos/service-result.png")


    # ports visuals
    ax = sb.countplot(x="PORT", data=df_of_open_ports,palette="Set2")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.figure.savefig("/home/kali/Desktop/src/photos/port-result.png")


    # state visuals
    ax = sb.countplot(x="STATE", data=df_of_open_ports,palette="Set2")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.figure.savefig("/home/kali/Desktop/src/photos/state-result.png")
    

#Report generation


    #images
    
    logo_img = "/home/kali/Desktop/src/photos/logo.png"
    service_img = "/home/kali/Desktop/src/photos/service-result.png"
    port_img = "/home/kali/Desktop/src/photos/port-result.png"
    multi_img = "/home/kali/Desktop/src/photos/multi-result.png"
    state_img = "/home/kali/Desktop/src/photos/state-result.png"

    #messages
    report_message4 = "Thank You for using the service..."
    report_message5 = "Cyber security team."
    report_message6 = "King Saud University - SEC 505 project"

    report_message7 = "Current features include:"
    report_message8 = "1. Collecting network data automatically"
    report_message9 = "2. Analyzing the collected network data"
    report_message10 = "3. Generate reports of the network status"
    new_feture1 = "4. Detect new discovered ports"
    new_feture2 = "5. Display warning message of the new detected ports"
    
    report_message1 ="Results of analyzing IP: " + host +" computer"
    report_message2 = "You have the following services running:"
    report_message3 = "You have some ports open! try to close unnecessarily ports:"
    state_message = "The state of running ports is shown below:"



    pdf = FPDF()
    #page1: Cover page
    pdf.add_page()
    pdf.set_font('Arial','B',22);
    pdf.set_text_color(173,216,230)

    pdf.cell(200, 10, txt = report_message1,ln = 1, align = 'C')
    pdf.image(logo_img, w=pdf.w/2.0, h=pdf.h/4.0,x=50)
    pdf.cell(200, 10, txt = report_message6,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = timenow,ln = 4, align = 'C')
        
    pdf.set_font('Arial','B',16);
    pdf.set_text_color(176,196,222)
    pdf.ln(25)
    pdf.cell(200, 10, txt = report_message7,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = report_message8,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = report_message9,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = report_message10,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = new_feture1,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = new_feture2,ln = 4, align = 'C')



    #page2: graphs
    pdf.add_page()
    pdf.set_text_color(0,76,153)
    
    pdf.cell(200, 10, txt = report_message2,ln = 2, align = 'C')
    pdf.image(service_img, w=pdf.w/2.0, h=pdf.h/4.0,x=50)
    pdf.ln(0.15)
    
    pdf.cell(200, 10, txt = state_message,ln = 3, align = 'C')
    pdf.image(state_img, w=pdf.w/2.0, h=pdf.h/4.0, x=50)
    pdf.ln(0.15)
   
    pdf.cell(200, 10, txt = report_message3,ln = 3, align = 'C')
    pdf.image(port_img, w=pdf.w/2.0, h=pdf.h/4.0, x=50)
    pdf.ln(0.15)

    #page 3: Conclude
    pdf.add_page()
    pdf.cell(200, 10, txt = report_message4,ln = 4, align = 'C')
    pdf.cell(200, 10, txt = report_message5,ln = 4, align = 'C')

    report_name = "final_report_"+timenow+".pdf"
    pdf.output("/home/kali/Desktop/src/reports/final_report.pdf",'F')



def anomaly_detection():


    #change name of current to the one provided by shell/py?
    myFolder = 'csv_data'
    files = []
    results = []
    susp_list = []

#new scan
    current_file_name = file_name
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
            try:
                df = pd.read_csv(myfile)
            except:
                continue;
                for port in current_file['PORT']:
                    if port not in df.values:
                        if port not in susp_list:
                            susp_list.append({'PORT': port})
            


    susp_df = pd.DataFrame(susp_list, columns = ['PORT'])


    for file in glob.glob('csv_data/*.csv'):
        if file == current_file_name:
            continue;
        files.append(file)

        with open(os.path.join(os.getcwd(),file),mode='r') as myfile:
            try:
                df = pd.read_csv(myfile)
            except:
                continue;
                for port in susp_df['PORT']:
                    if port in df.values:
                        susp_df = susp_df[susp_df.PORT != port]

        
    susp_df = susp_df.drop_duplicates()
#    results_df = pd.DataFrame(results, columns = ['PORT'])
    if len(susp_df)>0:
        print('\033[93m'+"\n WARNINIG: "+str(len(susp_df))+" NEW PORTS DETECTED!!"+'\033[0m')
        print(susp_df)
    else:
        print('NO NEW PORTS DETECTED..')


#main

def main():
    data_analysis()
    anomaly_detection()
    exit()

if __name__ == "__main__":
    main()
