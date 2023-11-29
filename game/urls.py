from django.urls import path
from game.views import index, play


# 调用view.index,字符串负责ip/a/b里面b的内容(a,b都可以为空)
urlpatterns = [
    path('', index, name = 'index'),
    path('play/', play, name = 'play')
]