import random
from datetime import date

number_digit = 10
min_value = 10 ** (number_digit - 1)
max_value = (10 ** number_digit) - 1


def image_uploader(instance, file_name):
    name, extension = file_name.split('.')
    random_number = random.randint(min_value, max_value)
    today = date.today()
    formatted_date = today.strftime("%m-%Y")
    try:
        op = instance.operation
        return f'Operation_images/{formatted_date}/patient_id_{instance.operation.patient.id}_{random_number}.{extension}'
    except:
        return f'{formatted_date}/patient_id_{instance.operation.patient.id}_obj_id_{instance.id}_{random_number}.{extension}'
