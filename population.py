import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')


import django
django.setup()

import random
from first_app.models import AccessRecords,Topic,Webpage
from faker import Faker as fk


fakegen  = fk()

topics=['Disease','Diet','Health']


def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):


    for entry in range(N):
        #get the topic for entry
        top=add_topic()


        #ceate the fake
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        #create fakewebpage

        webpg=Webpage.objects.get_or_create(topic=top,URL=fake_url,name=fake_name)[0]


        #create fake AccessRecords
        acc_rec=AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]



if __name__ == '__main__':
    print("population script!")
    populate(20)
    print("Population Done")
