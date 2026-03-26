from django.contrib import admin
from learning_logs.models import Topic, Entry
from chat_app.models import Chat

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Chat)