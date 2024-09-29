from django.contrib import admin

from backend.core.models import User, Company, Benefit, Category, ContractType, Job, Local, State

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(ContractType)
admin.site.register(Job)
admin.site.register(Local)
admin.site.register(State)