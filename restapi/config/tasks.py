import os
from celery import shared_task
from celery import Celery

from django.core.exceptions import ValidationError

@shared_task
def bulk_add_users(path):
    path = os.path.realpath("./restapi3/"+path)
    ext = os.path.splitext(path)[1] 
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    
    with open(path, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        _ = next(reader)
        for line in reader:
            username = line[0]
            email = line[1]
            password = line[2]
            print(username,email,password)
            if not (username and
                    email and
                    password):
                raise ValueError(f'Invalid User data!')
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
