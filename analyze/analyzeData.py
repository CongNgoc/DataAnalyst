import csv

def processMatrix(file_name):
    with open(file_name) as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=',');
        header = next(csv_reader);
        #Reading csv file again
        i = 0;
        for row in csv_reader:  
            print("----------------------");
            print(i);
            with open(file_name) as csv_data_cp:
                csv_reader_cp = csv.reader(csv_data_cp, delimiter=',');
                read_next = next(csv_reader_cp);
                read_next = next(csv_reader_cp);
                j = 0;
                for row_cp in csv_reader_cp:
                    print(j);   
                    if(row[6] != row_cp[6]):
                        print("row[6]: ", row[6]);
                        print("row_cp[6]: ", row_cp[6]);
                    j = j + 1;
            i = i + 1;
            

processMatrix(file_name = '../resource/CSV_output.csv');

#read csv file  and Save to dict 