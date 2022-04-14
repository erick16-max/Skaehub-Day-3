import numpy as np
current_month = str(input("Enter the current Month yyyy-mm:"))
next_month =str(input("Enter the next Month format yyyy-mm: "))

def get_number_of_weekdays(c_month, n_month):
    weekdays = np.busday_count(c_month, n_month)
 
    return weekdays

weekdays = get_number_of_weekdays(current_month, next_month)

print(f"The number of weekdays are {weekdays}")