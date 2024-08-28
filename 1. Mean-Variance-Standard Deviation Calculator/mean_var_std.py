import numpy as np

def calculate(lst):

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    ca = np.array(lst).reshape(3, 3)
    
    calculations = {
        'mean': [list(np.mean(ca, axis=0)), list(np.mean(ca, axis=1)), np.mean(lst)],
        'variance': [list(np.var(ca, axis=0)), list(np.var(ca, axis=1)), np.var(lst)],
        'standard deviation': [list(np.std(ca, axis=0)), list(np.std(ca, axis=1)), np.std(lst)],
        'max': [list(np.max(ca, axis=0)), list(np.max(ca, axis=1)), np.max(lst)],
        'min': [list(np.min(ca, axis=0)), list(np.min(ca, axis=1)), np.min(lst)],
        'sum': [list(np.sum(ca, axis=0)), list(np.sum(ca, axis=1)), np.sum(lst)]
    }


    return calculations