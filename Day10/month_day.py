def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        output = True
        return output
      else:
        output =False
        return output

    else:
      output =True
      return output

  else:
    output = False
    return output


def days_in_month(num_year , num_month ):

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(num_year) and num_month ==2 :
      return 29
      

    num_month = month_days[num_month-1] 
    return num_month
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







