#!/bin/sh


# ANSI colors for Auto-nmap-Analyzer
RED='\033[0;31m'
YELLOW='\033[0;33m'
CYAN='\033[36m'
GREEN='\033[0;32m'
NC='\033[0m'
BLUE='\033[0;34m'
origIFS="${IFS}"
REMOTE='off'
now=`date`

# Start timer
elapsedStart="$(date '+%H:%M:%S' | awk -F: '{print $1 * 3600 + $2 * 60 + $3}')"

HOST="45.33.32.156"
TYPE='PORT'


header() {
        echo
        # Print scan type
        printf "${CYAN}\t\t **** Auto-Nmap Analyzer **** \n\n"
        printf "${CYAN}\t **** SEC-505 (Network Security) Project **** \n\n"
        printf "${BLUE}Running a ${TYPE} scan on ${NC}${HOST}\n\n"
}


# Port Nmap port scan
portScan() {
        printf "${GREEN}---------------------Starting Port Scan-----------------------\n"
        printf "${NC}\n"
    
    if [ -e results"-${now}" ];
    then
    rm results"-${now}"
    fi
    
      nmap $HOST | tail -n +5 |head -n -3 >> results"-${now}"



      while read line
      do
      if [ line  = "open" ] && [ line  = "http" ];
then
      whatweb $HOST -v > temp
     fi
done <results"-${now}"

if [ -e temp ];
then
cat temp >> results"-${now}"
rm temp
fi

cat results"-${now}" | tr -s '[:blank:]' ',' > Data" On ${now}".csv
cat results"-${now}"
rm results"-${now}"

}

# Print footer with total elapsed time
footer() {

        printf "${GREEN}---------------------Finished all scans------------------------\n"
        printf "${NC}\n\n"

}


# Choose run type based on chosen flags

header
portScan
footer
python3 analysis.py Data" On ${now}".csv $HOST
evince final_report.pdf