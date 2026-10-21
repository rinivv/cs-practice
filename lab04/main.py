from stats import average_by_city, read_valid, warmest_city

import sys

lines = sys.stdin.read().splitlines()

valid_rec = read_valid(lines)
n_valid = len(valid_rec)
n_emp = sum(1 for line in lines if line == '')
n_invalid = len(lines) - n_valid - n_emp

city_ave = average_by_city(valid_rec)
if city_ave:
    warmest = warmest_city(valid_rec)
    res_temp = city_ave[warmest]
else:
    res_temp = 0.0
    warmest = ''
    
print(n_valid)
print(n_invalid)
print(f'{res_temp:.1f}')
