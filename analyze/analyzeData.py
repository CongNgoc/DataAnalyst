import csv
import readData as rd


# READ FILE AND PRINT DATA --- FOR DUBUG
def printData(file_name):
    data_arr = rd.writeCSV(file_name);
    count_high = 0;
    count_medium = 0;
    count_low = 0;
    index_to_get_data = 6;
    for order in data_arr:
        if order[index_to_get_data] == "Yes":
            count_high = count_high + 1;
        elif order[index_to_get_data] == "No":
            count_medium = count_medium + 1;
        # elif order[index_to_get_data] == "Low":
        #     count_low = count_low + 1;
        # print(order)
    print("count_high: " , count_high)
    print("count_medium: " , count_medium)
    print("count_low: " , count_low)
    print("sum: " , count_low + count_high + count_medium)


# PROCESSING MATRIX --- 2.2 IN SLIDE  
def processMatrix(data_arr):
    count = 0;
    diff_arr = [];
    for i in range(0, len(data_arr) - 1):
        order_i = data_arr[i];

        for j in range(i+1, len(data_arr)):
            diff_elements = [];
            order_j = data_arr[j];

            if(order_i[6] != order_j[6]):
                for index in range(0, len(order_i) - 1):
                    if(order_i[index] != order_j[index]):
                        diff_elements.append(index);
            if diff_elements:
                diff_arr.append(diff_elements);
    return diff_arr;


# REDUCE ARRAY TO SET(DOSE NOT HAVE DUPLICATE VALUE) AND FIND LOI~  --- 2.2.1 IN SLIDE  
def reduceArray(data_arr):
    diff_arr = sort_and_deduplicate(processMatrix(data_arr))
    i = 0;len_i = len(diff_arr) - 1;
    while i < len_i:
        list1 = diff_arr[i];     
        j = i + 1;len_j = len(diff_arr);

        while j < len_j:
            list2 = diff_arr[j];
            is_list1_contain_in_list2 = all(elem in list1  for elem in list2);
            is_list2_contain_in_list1 = all(elem in list2  for elem in list1);

            if(is_list1_contain_in_list2):
                diff_arr[i] = diff_arr[j];
                diff_arr.pop(i);                
                len_j = len_j - 1;
                len_i = len_i - 1;
                i = 0;
                break;

            elif(is_list2_contain_in_list1):
                diff_arr.pop(j);
                len_j = len_j - 1;
                len_i = len_i - 1;
                j = 0;
                break;

            j = j + 1;
        i = i + 1;
    return diff_arr;


# GET UNIQUE VALUE IN LIST
def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item


# SORT LIST
def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))


# PARSE MATRIX TO SINGLE VALUE IN ARRAY 
def parseMatrixToAraay(diff_arr):
    res_arr = [];
    for item in diff_arr:
        res_arr.append(item[0]);
    return res_arr;


#LAY TAT CA THUOC TINH TRONG DIFF_ARR RA
def getArrayToRoughSet(data_arr, diff_arr):
    arr_Yes = [];
    arr_No = [];
    for order in data_arr:
        diff_item = [];
        for index in diff_arr:
            diff_item.append(order[index]);
        diff_item.append(order[len(order) - 1]);

        if order[len(order) - 1] == "Yes":
            arr_Yes.append(diff_item);
        else:
            arr_No.append(diff_item);
        
    return arr_Yes, arr_No;


# Apply this function for the case is diff_arr have just unique value 
# Ex: diff_arr = [[1], [3]]  
def roughSets(roughSet_arr, diff_arr, file_output_name):
    file_output = open(file_output_name, 'w');

    header = ["MPG","Cylinders","Engine displacement","Horsepower",
        "Vehicle weight","Origin of car","Acceleration"];

    # Choose header add to result
    res_header = [];
    for index in diff_arr:
        res_header.append(header[index]);
   
    for order in roughSet_arr:
        str_res = "Neu ";
        for index in range(0, len(diff_arr)):
            str_res = str_res + res_header[index] + ' la "'  + order[index] + '" ';
        str_res = str_res + 'thi Acceleration la "' + order[len(order) - 1] + '"\n';

        file_output.write(str_res);


#FUNCTION TO ANALYZE DATA 
def runToAnalyzeData():
    file_input = '../resource/cars_data.txt';
    file_output_yes_value = '../resource/roughSetsForYesValue.txt';
    file_output_no_value = '../resource/roughSetsForNoValue.txt';

    data_arr = rd.writeCSV(file_input);
    diff_arr = parseMatrixToAraay(reduceArray(data_arr));
    arr_Yes, arr_No =  getArrayToRoughSet(data_arr, diff_arr)
    arr_Y = sort_and_deduplicate(arr_Yes)
    arr_N = sort_and_deduplicate(arr_No)

    roughSets(arr_Y, diff_arr, file_output_yes_value)
    roughSets(arr_N, diff_arr, file_output_no_value)
    print("Analyze Successsfuly!")
 


#ANALYZE DATA 
runToAnalyzeData()
