
def parseStringToFloat(value_cylinders):
    result_value = 0;
    is_value_null = True;

    if(value_cylinders != "NA"):
        result_value = float(value_cylinders);
        is_value_null = False;

    return result_value, is_value_null;

def readFileToDict(file_txt_input):
    with open(file_txt_input,'r') as f:
        data_result = []
        for line in f:
            order = []
            for item in line.split():
                order.append(item);
            data_result.append(order);
    return data_result;

def caculateAverage(value_ele,is_value_null):
    sum_MPG = sum_MPG + value_ele;
    if(is_value_null is False):
        number_of_real_item = number_of_real_item + 1;

def caculateAverageAllValue():
    data_result = readFileToDict("../resource/cars_data.txt");

    sum_MPG = 0;sum_Eng = 0;sum_Hor = 0;sum_Veh = 0;sum_Acce = 0;
    #count number of real item of element(MPG, Cylinders,..)
    num_of_MPG = 0;num_of_Eng = 0;num_of_Hor = 0;num_of_Veh = 0;num_of_Acce = 0;
    averages = []

    for k,order in enumerate(data_result):
        for index, item in enumerate(order):
            if(index == 0):
                value_ele,is_value_null = parseStringToFloat(item);
                sum_MPG = sum_MPG + value_ele;
                if(is_value_null is False):
                    num_of_MPG = num_of_MPG + 1;
            elif(index == 2):
                value_ele,is_value_null = parseStringToFloat(item);
                sum_Eng = sum_Eng + value_ele;
                if(is_value_null is False):
                    num_of_Eng = num_of_Eng + 1;
            elif(index == 3):
                value_ele,is_value_null = parseStringToFloat(item);
                sum_Hor = sum_Hor + value_ele;
                if(is_value_null is False):
                    num_of_Hor = num_of_Hor + 1;
            elif(index == 4):
                value_ele,is_value_null = parseStringToFloat(item);
                sum_Veh = sum_Veh + value_ele;
                if(is_value_null is False):
                    num_of_Veh = num_of_Veh + 1;
            elif(index == 5):
                value_ele,is_value_null = parseStringToFloat(item);
                sum_Acce = sum_Acce + value_ele;
                if(is_value_null is False):
                    num_of_Acce = num_of_Acce + 1;

    #caculate average for all value
    averages.extend([sum_MPG/num_of_MPG, sum_Eng/num_of_Eng, sum_Hor/num_of_Hor, sum_Veh/num_of_Veh, sum_Acce/num_of_Acce]);
    return averages;
