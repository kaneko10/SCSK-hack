from django.contrib import admin

# /admin でデータベースの中身を確認するには、ここにモデル名を追加する必要がある

from .models import User, Number

admin.site.register(User)
admin.site.register(Number)