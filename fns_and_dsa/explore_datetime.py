from datetime import datetime, timedelta


def display_current_datetime():
  current_date = datetime.now()
  print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S")) 

# .strftime is a method used with Python's datetime objects to format dates and times as strings. 
# It allows you to specify the output format using format codes (like %Y for year, %m for month, %d for day, etc.).

def calculate_future_date():
  days = int(input("Enter the number of days to add: "))
  # if days < 0:
  #   print("Please enter a non-negative number of days.")
  #   return
  # current_date = datetime.now()
  future_date = datetime.now() + timedelta(days=days)
  print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
  display_current_datetime()
  calculate_future_date()