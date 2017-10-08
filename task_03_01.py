from datetime import datetime

def get_days_to_new_year():
    day_now = datetime.today()
    new_year = day_now.year+1
    new_year_date = datetime(new_year, 1, 1)
    time_to_new_year = new_year_date - day_now
    days_to_new_year = int(time_to_new_year.days)
#    days_to_new_year = int((datetime(datetime.today().year+1, 1, 1) - datetime.today()).days)
    return days_to_new_year

if (__name__=="__main__"):
    print(get_days_to_new_year())
