import numpy as np
from fractions import Fraction

def identity(n):
  new_matrix = []
  for i in range(0,n):
    new_row = []
    for j in range(0,n):
      new_row.append(1.0 if i == j else 0.0)
    new_matrix.append(new_row)
  return new_matrix

def normalize(matrix, row_sums):
    column_count = len(matrix[0])
    row_count = len(matrix)
    normalized_matrix = []
    for row_idx in range(0, row_count):
        normalized_row = []
        for col_idx in range(0, column_count):
            normalized_row.append(float(matrix[row_idx][col_idx]) / float(row_sums[row_idx]))
        normalized_matrix.append(normalized_row)
    return normalized_matrix
    
def lcm(x,y):
    greater = x if x > y else y
    while(True):
        if((greater % x) == 0 and (greater % y == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

def solution(n):
    row_sums = []
    non_abs_states = 0
    non_abs_rows = []
    non_abs_rows_idxs = []
    abs_rows = []
    abs_rows_idxs = []
    total_sum = 0
    for idx,row in enumerate(n):
        quick_sum = sum(row)
        total_sum = total_sum + quick_sum
        if quick_sum > 0:
            non_abs_states = non_abs_states + 1
            non_abs_rows.append(row)
            non_abs_rows_idxs.append(idx)
            row_sums.append(quick_sum)
        else:
            abs_rows.append(row)
            abs_rows_idxs.append(idx)
    
    new_order = non_abs_rows_idxs + abs_rows_idxs
    new_matrix = []
    for row in non_abs_rows:
        new_row = []
        for idx in new_order:
            new_row.append(row[idx])
        new_matrix.append(new_row)
    
    if sum(n[0]) == 0:
        result = [1]
        zeroes = [0] * (len(n) - non_abs_states - 1)
        return result + zeroes + result
    if total_sum == 0 or sum(n[0]) == 0:
        result = [1]
        zeroes = [0] * (len(n) - 1)
        return result + zeroes + result
    if len(n) < 3:
        return [1,1]
    
    q_r = normalize(new_matrix, row_sums)
    q = []
    r = []
    for elem in q_r:
      real_q = elem[:non_abs_states]
      q.append(real_q)
      real_r = elem[non_abs_states:]
      r.append(real_r)
      
    i = identity(len(q))
    n = np.linalg.inv(np.subtract(i,q))
    m = np.dot(n,r)
    results_as_frac = []
    results = []
    denominators = []
    common_denom = 0
    for elem in m[0]:
        x = Fraction(elem).limit_denominator(1000000000000)
        results_as_frac.append(x)
        denominators.append(x.denominator)
    common_denom = denominators[0]
    for idx in range(0, len(denominators)):
        common_denom = lcm(common_denom, denominators[idx])
    for elem in results_as_frac:
        newmerator = elem.numerator * (common_denom/elem.denominator)
        results.append(newmerator)
    results.append(common_denom)
    
    return results
    