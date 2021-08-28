import codecs

from scraping.parsers import *

parsers = (
    (work, 'https://www.work.ua/ru/jobs-dnipro-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%94%D0%BD%D0%B5%D0%BF%D1%80&category=Python'),
    (rabota,
     'https://rabota.ua/zapros/python/%D0%B4%D0%BD%D0%B5%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA'),
    (djinni, 'https://djinni.co/jobs/keyword-python/dnipro/')
)

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
