

get_num = int(input())
leap_year = get_num % 2
if(leap_year == 0):
  print(str(get_num) + " it is leap year")
else:
  print(str(get_num) + " it is not leap year")