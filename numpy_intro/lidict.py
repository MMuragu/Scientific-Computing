def list_stats(numbers):
    try:
        stats = {
            'min': min(numbers),
            'max': max(numbers),
            'average': sum(numbers)/len(numbers)
        }
        return stats
    except TypeError:
        return "Error: All elements must be numeric"
    except ValueError:
        return "Error: List cannot be empty"
print(list_stats([2, 5, 'a', 9]))  

print(list_stats([1, 2, 3, 4, 5]))  # {'min': 1, 'max': 5, 'average': 3.0}
print(list_stats([]))       # Error message