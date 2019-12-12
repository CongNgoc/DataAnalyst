import csv
import processingData as pr

averages = pr.caculateAverageAllValue()

def caculateValue(value_of_element, low_value, high_value, average_value):
    result_value = "";
    value_of_element = float(value_of_element) if(value_of_element != "NA") else float(average_value);

    if(value_of_element < low_value):
        result_value = "Low";
    elif(value_of_element >= high_value):
        result_value = "High";
    else:
        result_value = "Medium";

    return result_value

def setValueForMainAttribute(value_of_element, value, average_value):
    rresult_value = "";
    value_of_element = float(value_of_element) if(value_of_element != "NA") else float(average_value);

    if(value_of_element < value):
        result_value = "No";
    else:
        result_value = "Yes";

    return result_value

def checkNullOfValue(value_cylinders):
    result_value = 0;
    if(value_cylinders != "NA"):
        result_value = float(value_cylinders);
    return result_value

def setOriginOfCar(value_of_element):
    result_value = 0;
    if(value_of_element != "NA"):
        value_of_element = float(value_of_element);
        if(value_of_element == 1.0):
            result_value = "American";
        elif(value_of_element == 2.0):
            result_value = "European";
        else:
            result_value = "Japanese";
    return result_value

def writeCSV(file_txt_input):
    file_csv_output = '../resource/CSV_output.csv';
    print("Start parse data!");

    data_result = [];
    csv_data = open(file_csv_output, 'w');
    json_data = '';
    # create the csv writer object
    csvwriter = csv.writer(csv_data);
    csvwriter.writerow(["MPG", "Cylinders", "Engine displacement", "Horsepower", "Vehicle weight", "Origin of car","Acceleration"]);
    
    with open(file_txt_input,'r') as f:
        for line in f:
            column_number = 0;
            data_each_row = [];
            decided_attr = "";
            for word in line.split():               
                if(column_number == 0):
                    word = caculateValue(value_of_element = word, low_value = 20, 
                        high_value = 30, average_value = averages[0]);
                    data_each_row.append(word);
                    
                # elif(column_number == 1):
                #     word = checkNullOfValue(word);
                #     data_each_row.append(word);
                elif(column_number == 1):
                    word = caculateValue(value_of_element = word, low_value = 4, 
                        high_value = 6, average_value = 5);
                    data_each_row.append(word);

                elif(column_number == 2):
                    word = caculateValue(value_of_element = word, low_value = 200, 
                        high_value = 300, average_value = averages[1]);
                    data_each_row.append(word);

                elif(column_number == 3):
                    word = caculateValue(value_of_element = word, low_value = 100, 
                        high_value = 150, average_value = averages[2]);
                    data_each_row.append(word);

                elif(column_number == 4):
                    word = caculateValue(value_of_element = word, low_value = 3000, 
                        high_value = 4000, average_value = averages[3]);
                    data_each_row.append(word);

                elif(column_number == 5):
                    decided_attr = setValueForMainAttribute(value_of_element = word, 
                        value = 10, average_value = averages[4]);
                                        
                elif(column_number == 7):
                    word = setOriginOfCar(word);
                    data_each_row.append(word);
                    data_each_row.append(decided_attr);

                column_number = column_number + 1;
            csvwriter.writerow(data_each_row);
            data_result.append(data_each_row);
    print("Parse successful!");
    return data_result;

#file_txt_input = '../resource/cars_data.txt';
#print(writeCSV(file_txt_input);
