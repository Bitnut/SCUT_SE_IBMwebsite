# encoding:utf-8
from django.shortcuts import render
from default.models import RegisterTable


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def join_page(request):
    return render(request, 'join.html')


def about_page(request):
    return render(request, 'about.html')


def learnmore_page(request):
    return render(request, 'lib.html')


def lib_page(request):
    return render(request, 'lib.html')


def join(request):

    if request.method == 'GET':
        return render(request, 'join.html')

    print request.POST['agree_to_allocation']

    RegisterTable.objects.create(
        # 姓名
        name=request.POST['name'],
        # 性别
        sex=request.POST['sex'],
        # 民族
        nation=request.POST['nation'],
        # 电话
        phone=request.POST['phone'],
        # email
        email=request.POST['email'],
        # qq
        qq=request.POST['QQ'],
        # 爱好
        hobby=request.POST['hobby'],
        # 宿舍地址
        address=request.POST['address'],
        # 学生组织
        organization=request.POST['organization'],
        # 技术倾向
        tech=request.POST['tech'],
        # 申请部门
        apartment=request.POST['apartment'],
        # 是否服从分配
        agree_to_allocation=request.POST['agree_to_allocation'],
        # 期待
        await=request.POST['await'],
        # 大学的计划
        plan=request.POST['plan'],
        # 自我评价
        assess=request.POST['assess'],
    )
    return render(request, 'result.html',
                  {
                      'result_title': '报名成功',
                      'result_picture_name': 'success.png',
                      'result_text_p1': '确认邮件将会在一天内发送 如未收到请发送邮件至wangboquan220116@outlook.com',
                      'result_text_p2': '具体面试时间将以短信和邮件的形式通知'
                  })

