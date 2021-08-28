import codecs
import os, sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django

django.setup()

from scraping.parsers import *

from scraping.models import Vacancy, City, Language, Error

parsers = (
    (work, 'https://www.work.ua/ru/jobs-dnipro-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%94%D0%BD%D0%B5%D0%BF%D1%80&category=Python'),
    (rabota,
     'https://rabota.ua/zapros/python/%D0%B4%D0%BD%D0%B5%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA'),
    (djinni, 'https://djinni.co/jobs/keyword-python/dnipro/')
)
city = City.objects.filter(slug='dnepr').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e
for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError():
        pass
if errors:
    er = Error(data=errors).save()
    # h = codecs.open('work.txt', 'w', 'utf-8')
    # h.write(str(jobs))
    # h.close()
