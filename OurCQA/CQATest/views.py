from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from  django.http import  HttpResponse#封装响应
from django.template import Context#对响应数据进行封装
from django.template.loader import get_template#加载模板
# Create your views here.
# def index(request):
#     # return HttpResponse('Hello world!')
#     return render_to_response('index.html')
address = [('张三', '地址一'), ('李四', '地址二') ]
def index(request):
    """
    :param request:用户来接收用户的请求，用户自动传递
    :return: response响应
    """
    template = get_template("index.html")
    return HttpResponse(template.render({'data':address[0]}))