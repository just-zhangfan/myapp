from django.http import HttpResponse


# 接收用户请求时，会被调用，并返回响应
def index(request):
    line1 = '<h1 style="text-align:center">我的第一个网页</h1>'
    line3 = '<hr>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<img src="https://ts1.cn.mm.bing.net/th/id/R-C.412c861057e922cd2945288440ce5ec6?rik=9e5nkAgDwiSrVg&riu=http%3a%2f%2fimgboys2.yohob\
        uy.com%2fcontentimg%2f2018%2f08%2f09%2f10%2f02d2df4502365fbbe13f1e82740e86e1d5.jpg&ehk=rVv0vNbzqSS2HhbqaJnCho3MbTWVw%2by6qWHBd8RmKMA%3d&risl=&pid=ImgRaw&r=0"\
        width=300px>'
    return HttpResponse(line1 + line3 + line4 + line2)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line3 = '<a href="/">返回主界面</a>'
    line2 = '<img src="https://pic3.zhimg.com/v2-9a1f0fd7ac990f97364471b7217b70d6_r.jpg?source=1940ef5c">'
    return HttpResponse(line1 + line3 + line2)