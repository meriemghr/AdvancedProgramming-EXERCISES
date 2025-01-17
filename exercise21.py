def length(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    return len(lst)


def mean(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
      
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numeric values.")
    
    return sum(lst) / len(lst)


def range_of_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
      
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numeric values.")
    
    return max(lst) - min(lst)


# the bonus functions
def median(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")

    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numeric values.")
    
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    mid = n // 2
    
    if n % 2 == 0:
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]


def standard_deviation(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")

    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numeric values.")
    
    mean_val = mean(lst)
    variance = sum((i - mean_val) ** 2 for i in lst) / len(lst)
    return variance ** 0.5


def list_statistics(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")

    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numeric values.")
    
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }

numbers = [1, 2, 3, 4, 5]
print(length(numbers))  
print(mean(numbers))
print(range_of_list(numbers)) 
print(median(numbers)) 
print(standard_deviation(numbers))  
print(list_statistics(numbers))  

print(length([])) 
print(mean([5])) 
print(range_of_list([-3, -1, -7])) 
print(median([3.5, 1.2, 5.8]))  
print(standard_deviation([1.0, 2.0, 3.0]))  

