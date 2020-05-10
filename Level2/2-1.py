def solution(L):
  print(L)
  asc = L
  L.sort()
  print(L)
  current_sum = 0
  l_string = ''
  while len(asc) > 0:
    print(asc)
    for elem in asc:
      current_sum = current_sum + elem
    print(current_sum)
    if current_sum % 3 == 0:
      for num in asc:
        l_string = l_string + str(num) 
      return(int(l_string))
    for elem in asc:
      print(asc)
      cond_check = current_sum if len(asc) <= 1 else (current_sum - elem)
      if cond_check % 3 == 0:
        print(elem)
        asc.remove(elem)
        for num in asc:
          l_string = l_string + str(num)
          if len(asc) == 0:
            l_string = str(elem)
          return(int(l_string))
        l_string = ''
    current_sum = 0
    asc.pop(0)
  return 0