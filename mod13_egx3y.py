import datetime
symbol = input("Enter Symbol in all caps: ") 
if symbol.isalpha() == True and len(symbol) <= 7 and symbol.isupper() == True:
  print("Valid Symbol") 
else:
  print("Invalid Symbol") 

try:
  chart_type = int(input("Enter Chart Type (1 OR 2): ")) 
  if chart_type == 1 or chart_type == 2:  
    print("Valid Chart Type") 
  else:
    print("Invalid Chart Tyle")  
except ValueError:
  print("Invalid Chart Type")  

try:
  time_series = int(input("Enter Time Series (1-4): ")) 
  if time_series > 0 and time_series < 5:  
    print("Valid Time Series") 
  else:
    print("Invalid Time Series") 
except ValueError:
  print("Invalid Time Series") 

date_string = input("Enter Start Date: YYYY-MM-DD ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("Valid Date Entered") 
except ValueError:
  print("Input not valid, enter in the format of YYYY-MM-DD Format")

date_string = input("Enter End Date: YYYY-MM-DD ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) 
  print("Valid Date Entered") 
except ValueError:
  print("Input not valid, enter in the format of YYYY-MM-DD Format")