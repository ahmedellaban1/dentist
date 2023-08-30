from datetime import date, datetime

# Create your views here
def get_date():
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return formatted_date


def get_time():
    now = datetime.now()
    return f'{now.strftime("%H:%M")}'
