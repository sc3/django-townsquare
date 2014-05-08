
from datetime import date, time, datetime
import random, string


def time_today(hour):
    return datetime.combine(datetime.now(), time(hour=hour))


def gen_password(length=8):
    myrg = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pw = str().join(myrg.choice(alphabet) for c in range(length))
    return pw

    
def gen_username(first_name, last_name, signup_date):
    return '{0}{1}:{2}'.format(
            first_name, last_name, signup_date.strftime('%m-%d-%y'))


