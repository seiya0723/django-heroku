from django.shortcuts import render

# Create your views here.

#クラスベースのビューを作るため
from django.views import View

#Viewを継承してGET文、POST文の関数を作る
class HomeView(View):

    def get(self, request, *args, **kwargs):

        return render(request,"home/index.html")

index   = HomeView.as_view()

