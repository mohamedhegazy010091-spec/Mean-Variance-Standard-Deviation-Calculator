## ====================================================================================
#                             ***  My own test case.   ***
# ====================================================================================
# import numpy liberary
import numpy as np

# defination of the function calculate
def calculate (numbers):
    # check if the lenth of the input list is not equal to 9
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers!")
    # convert the input list to a 3x3 numpy array
    matrix = np.array(numbers).reshape(3,3)
    #========================================================
    # Method 1: Using np.round to round the results to 2 decimal places
    #========================================================

    # calculations = {
    #       'Mean': [list(np.round(matrix.mean(axis=0),2)),  
    #              list(np.round(matrix.mean(axis=1),2)),   
    #              round(matrix.mean(),2)],          
    #     'Variance': [list(np.round(matrix.var(axis=0),2)),
    #                  list(np.round(matrix.var(axis=1),2)),
    #                  round(matrix.var(),2)],
    #     'Std Dev': [list(np.round(matrix.std(axis=0),2)),
    #                 list(np.round(matrix.std(axis=1),2)),
    #                 round(matrix.std(),2)],
    #     'Max': [list(np.round(matrix.max(axis=0),2)),
    #             list(np.round(matrix.max(axis=1),2)),
    #             round(matrix.max(),2)],
    #     'Min': [list(np.round(matrix.min(axis=0),2)),    
    #             list(np.round(matrix.min(axis=1),2)),
    #             round(matrix.min(),2)],
    #     'Sum': [list(np.round(matrix.sum(axis=0),2)),
    #             list(np.round(matrix.sum(axis=1),2)),
    #             round(matrix.sum(),2)]                      
    # }

    #========================================================
    # Method 2: Using .tolist() to convert numpy arrays to lists
    #========================================================
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), 
                 matrix.mean(axis=1).tolist(), 
                 matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(),
                     matrix.var(axis=1).tolist(),
                     matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(),
                               matrix.std(axis=1).tolist(),
                               matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(),
                matrix.max(axis=1).tolist(),
                matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(),
                matrix.min(axis=1).tolist(),
                matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(),
                matrix.sum(axis=1).tolist(),
                matrix.sum().tolist()]
    }

    return calculations




from mean_var_std import calculate
from pprint import pprint
number = [0,1,2,3,4,5,6,7,8]
pprint(calculate(number))
