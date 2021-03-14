from django.contrib import admin
from .models import User, Lead, Agent, Userprofile, Category


admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(Userprofile)
admin.site.register(Category)
