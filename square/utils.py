from datetime import date, time, datetime

def timedelta(time1, time2):
    start_date = dateize(time1)
    end_date = dateize(time2)
    return start_date-end_date

def dateize(time):
    return datetime.combine(date.today(), time)
