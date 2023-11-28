from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import User, Number
from .forms import UserForm
import json

# Create your views here.

class IndexView(View):
   def get(self, request):
      form = UserForm()
      return render(request, 'index.html', {'form': form})
   
   def post(self, request):
      # ボタンのname属性、value属性の値でポストリクエストを識別
      if 'decision' in request.POST:
         form = UserForm(request.POST)
         if form.is_valid():
            
            form.save()  # フォーム（forms.py）を利用している場合はこの方法でデータベースに保存できます
            form = UserForm()  # フォームを初期化

         users = User.objects.all()
         context = {    # contextで遷移先のページ（index.html）に変数を渡すことができます
               'form': form, 
               'users': users,
         }
         return render(request, 'index.html', context)
      elif 'toPage1' in request.POST:
         context = {
            # 渡したい変数
         }
         return render(request, 'page1.html', context)
      elif 'toPage2' in request.POST:
         context = {
            # 渡したい変数
         }
         return render(request, 'page2.html', context)
   

# ボタンを押すごとに数字を2倍していくページ
class Page1View(View):
   def get(self, request):
      template = loader.get_template("page1.html")
      context = {
         'num': 0,
      }
      return HttpResponse(template.render(context, request))
   def post(self, request):
      data = json.loads(request.body.decode('utf-8'))  # JSONデータを解析
      action = data.get('action')   # page1.htmlのcontextで送信した内容（37〜40行目）
      num = data.get('num')

      if action == "twice":
         num = self.twice(num)
         template = loader.get_template("page1.html")
         context = {
            'num': num,
         }
         return JsonResponse(context)
      elif action == "save":
         Number.objects.create(  # データベースに保存
            num = num,
         )
         context = {
            'num': num,
         }
         return JsonResponse(context)
      
   def twice(self, num):
      return 2 * num
   

class Page2View(View):
   def get(self, request):
      template = loader.get_template("page2.html")
      context = {
         # 渡したい変数
      }
      return HttpResponse(template.render(context, request))