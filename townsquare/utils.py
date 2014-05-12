
from datetime import date, time, datetime
import random, string


def timeonly_delta(timea, timeb):
    datea = datetime.combine(datetime.today(), timea)
    dateb = datetime.combine(datetime.today(), timeb)
    delta = datea - dateb
    return delta.seconds / 3600.0


def gen_password(length=8):
    myrg = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pw = str().join(myrg.choice(alphabet) for c in range(length))
    return pw

    
def gen_username(full_name, signup_date):
    return '{0}:{1}'.format(full_name, signup_date.strftime('%m-%d-%y'))
