import csv
import readData as rd

def printData(file_name):
    data_arr = rd.writeCSV(file_name);
    for order in data_arr:
        print(order);

def processMatrix(file_name):
    data_arr = rd.writeCSV(file_name);
    count = 0;
    diff_arr = [];
    for i in range(0, len(data_arr) - 1):
        order_i = data_arr[i];

        for j in range(i+1, len(data_arr)):
            diff_elements = [];
            order_j = data_arr[j];

            if(order_i[6] != order_j[6]):
                for index in range(0, len(order_i) - 2):
                    if(order_i[index] != order_j[index]):
                        diff_elements.append(index);
            if diff_elements:
                diff_arr.append(diff_elements);
    return diff_arr;

def reduceArray(file_name):
    diff_arr = processMatrix(file_name);
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
                diff_arr.pop(i);

                len_j = len_j - 1;
                len_i = len_i - 1;

            j = j + 1;
        i = i + 1;
    print(diff_arr);

def listToSet(diff_arr):
    return set(diff_arr);

def test():
    #diff_arr = [[1, 2, 3], [1, 2], [5,6,7]];
    diff_arr = [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5], [1, 3], [2, 3, 4, 5], [2, 3], [2], [10, 11]]
    i = 0;len_i = len(diff_arr) - 1;
    while i < len_i:
        print(i)
        list1 = diff_arr[i];
        
        j = i + 1;len_j = len(diff_arr);
        while j < len_j:

            list2 = diff_arr[j];
            is_list1_contain_in_list2 = all(elem in list1  for elem in list2);
            is_list2_contain_in_list1 = all(elem in list2  for elem in list1);
            print("contain1: ", is_list1_contain_in_list2);
            print("contain2: ", is_list2_contain_in_list1);

            # if(is_list1_contain_in_list2):
            #     diff_arr[i] = diff_arr[j];
            #     diff_arr.pop(i);
                
            #     len_j = len_j - 1;
            #     len_i = len_i - 1;

            #     i = 0;
            #     break;
            #     print("helllp")

            # elif(is_list2_contain_in_list1):
            #     diff_arr.pop(j);
            #     print("helllp1")

            #     len_j = len_j - 1;
            #     len_i = len_i - 1;

                # i = 0;
                # break;
            j = j + 1;
        i = i + 1;
    print(diff_arr);

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

def testSet():
    arr = [3, 3, 2, 3, 5, 9, 5, 9, 3, 2, 1, 0, 10, 15, -1]
    return set(arr)
file_name = '../resource/cars_data.txt';
# reduceArray(file_name);
# test();
# print(listToSet(processMatrix(file_name)));
print(sort_and_deduplicate(processMatrix(file_name)));

#printData(file_name = '../resource/cars_data_little.txt');
#read csv file  and Save to dict 

# DEBUG NGAY CHO CONTAIN