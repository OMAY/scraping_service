from django.contrib import admin

from scraping.models import City, Language, Vacancy, Error

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(Error)


