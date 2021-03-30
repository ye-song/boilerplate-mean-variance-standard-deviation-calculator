import numpy as np

def calculate(list):
    
    length = len(list)
    if length < 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.reshape(list, (3,3))
    
    calculations = {}

    #calculating mean    
    mean_row = np.mean(array,axis=0)
    mean_col = np.mean(array,axis=1)
    mean_value = np.mean(array)
    calculations["mean"] =[mean_row.tolist(), mean_col.tolist(), mean_value.tolist()]

    #calculating variance
    var_row = np.var(array, axis=0)
    var_col = np.var(array, axis=1)
    var = np.var(array)
    calculations["variance"] = [var_row.tolist(), var_col.tolist(), var.tolist()]

    #calculating standard deviation
    std_row = np.std(array, axis=0)
    std_col = np.std(array, axis=1)
    std = np.std(array)
    calculations["standard deviation"] = [std_row.tolist(), std_col.tolist(), std.tolist()]

    #calculating max
    max_row = np.max(array, axis=0)
    max_col = np.max(array, axis=1)
    max_value = np.max(array)
    calculations["max"] = [max_row.tolist(), max_col.tolist(), max_value.tolist()]

    #calculating min
    min_row = np.min(array, axis=0)
    min_col = np.min(array, axis=1)
    min_value = np.min(array)
    calculations["min"] = [min_row.tolist(), min_col.tolist(), min_value.tolist()]

    #calculating sum
    sum_row = np.sum(array, axis=0)
    sum_col = np.sum(array, axis=1)
    sum = np.sum(array)
    calculations["sum"] = [sum_row.tolist(), sum_col.tolist(), sum.tolist()]

    return calculations
