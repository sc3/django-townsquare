
from datetime import date, time, datetime
import random, string


def timeonly_delta(time1, time2):
    start_date = dateize(time1)
    end_date = dateize(time2)
    return start_date-end_date


def dateize(time):
    return datetime.combine(date.today(), time)


def gen_password(length=8):
    myrg = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pw = str().join(myrg.choice(alphabet) for c in range(length))
    return pw

    
def gen_username(first_name, last_name, date):
    return '{0}{1}:{2}'.format(
            first, last, v.signup_date.strftime('%m-%d-%y'))


