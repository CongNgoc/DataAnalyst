import csv
import readData as rd


# READ FILE AND PRINT DATA --- FOR DUBUG
def printData(file_name):
    data_arr = rd.writeCSV(file_name);
    count_high = 0;
    count_medium = 0;
    count_low = 0;
    index_to_get_data = 0;
    for order in data_arr:
        if order[index_to_get_data] == "High":
            count_high = count_high + 1;
        elif order[index_to_get_data] == "Medium":
            count_medium = count_medium + 1;
        elif order[index_to_get_data] == "Low":
            count_low = count_low + 1;
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


# Apply this function for the case is diff_arr have just unique value 
# Ex: diff_arr = [[1], [3]]  
def roughSets(data_arr, diff_arr, file_output_name):
    file_output = open(file_output_name, 'w');
    check_size_equals_1 = True
    header = ["MPG","Cylinders","Engine displacement","Horsepower",
        "Vehicle weight","Origin of car","Acceleration"];

    for diff_v in diff_arr:
        if len(diff_v) > 1:
            check_size_equals_1 = False

    if check_size_equals_1:
        for order in data_arr:
            str_res = "Neu ";
            for item in diff_arr:
                index = item[0];
                str_res = str_res + header[index] + ' la "'  + str(order[index]) + '" ';

            str_res = str_res + "thi ket qua la " + order[6] + " \n";
            print(str_res)
            file_output.write(str_res)

#FUNCTION TO ANALYZE DATA 
def runToAnalyzeData():
    file_input = '../resource/cars_data.txt';
    file_output = '../resource/roughSets.txt';
    data_arr = rd.writeCSV(file_input);
    diff_arr = reduceArray(data_arr)
    roughSets(data_arr, diff_arr, file_output)

runToAnalyzeData()
