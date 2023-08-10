# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"F41..11","system":"readv2"},{"code":"F413100","system":"readv2"},{"code":"F413200","system":"readv2"},{"code":"F41y000","system":"readv2"},{"code":"F41z.00","system":"readv2"},{"code":"1202.0","system":"med"},{"code":"1551.0","system":"med"},{"code":"1552.0","system":"med"},{"code":"21067.0","system":"med"},{"code":"24347.0","system":"med"},{"code":"24440.0","system":"med"},{"code":"2484.0","system":"med"},{"code":"2496.0","system":"med"},{"code":"29800.0","system":"med"},{"code":"30514.0","system":"med"},{"code":"32028.0","system":"med"},{"code":"34183.0","system":"med"},{"code":"34373.0","system":"med"},{"code":"35250.0","system":"med"},{"code":"38407.0","system":"med"},{"code":"38463.0","system":"med"},{"code":"4232.0","system":"med"},{"code":"45509.0","system":"med"},{"code":"47730.0","system":"med"},{"code":"50694.0","system":"med"},{"code":"53020.0","system":"med"},{"code":"53021.0","system":"med"},{"code":"55469.0","system":"med"},{"code":"61965.0","system":"med"},{"code":"62773.0","system":"med"},{"code":"62901.0","system":"med"},{"code":"6836.0","system":"med"},{"code":"71651.0","system":"med"},{"code":"72901.0","system":"med"},{"code":"8506.0","system":"med"},{"code":"8691.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('retinal-detachments-and-breaks-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["retinal-detachments-and-breaks---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["retinal-detachments-and-breaks---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["retinal-detachments-and-breaks---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
