import re
import datetime

def check_name(name: str):
    if not name or not name.isalpha():
        return 0
    return 1



def check_date(date):
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.datetime.strptime(date, date_format)
        return 1
    except ValueError:
        return 0
    
def check_email(mail: str):
    req_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    pattern = re.compile(req_pattern)
    if not re.match(pattern, mail):
        return 0
    return 1

def check_phone(phone: str):
    #req_pattern = r"^(01[0-9]{9})$/"
    #^(012|011|010)[0-9]{8}$

    req_pattern =r'^(01)[2|1|0|5][0-9]{8}$'
    pattern = re.compile(req_pattern)
    if not re.match(pattern, phone):
        return 0
    return 1