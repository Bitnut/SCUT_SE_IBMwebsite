# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.shortcuts import render, render_to_response
from . import models
from django.urls import reverse
from .models import User, project_user, Project
from django.shortcuts import get_object_or_404, render
import json
from models import user_commit


from . import GitFileController
import os.path
from django.views.decorators.csrf import csrf_exempt


#服务器仓库地址，所有用户所在的目录
codehub_path = os.path.dirname(__file__)+'/repo/'


# Create your views here.
def index(request):
    return render(request,'index.html')

def mainPage(request):
    return render(request,'mainPage.html')


def code_test(request):
    return render(request,'code.html')


def code(request):
    print '进入代码界面'

    p_owner,p_name = request.GET.get('project_owner'),request.GET.get('project_name')
    if p_owner == None:
        p_owner,p_name = request.session['now_project_owner'],request.session['now_project_name']
    print p_owner,p_name
    project = Project.objects.get(project_name=p_name,lead_user=p_owner)
    #project = Project.objects.get(project_id=res)
    request.session['now_project_id'] = project.project_id
    request.session['now_project_id'] = project.project_id
    request.session['now_project_description'] = project.description
    request.session['now_project_owner'] = project.lead_user.user_name
    request.session['now_project_repo_path'] = codehub_path + project.lead_user.user_name + '/'+project.project_name+'/'

    #is_leader才能有设置界面，删除项目
    if request.session['now_project_owner'] == request.session['user_name']:
        request.session['is_leader'] = True
    else: request.session['is_leader'] = False

    files = os.listdir(request.session['now_project_repo_path'])
    print (files)
    
    head_branch = GitFileController.mygit.get_head_branch(request.session['now_project_repo_path']).split('/')[-1]
    request.session['head_branch']=head_branch
    print (codehub_path + project.repo_path)
    data = GitFileController.mygit.show_branches_refs(request.session['now_project_repo_path'])
    return render(request, 'code.html', {'project': project,'files': files,'data':data})




def code_switch_branch(request):
    print '切换分支'
    tobranch = request.POST.get('tobranch')
    GitFileController.mygit.switch_branch(request.session['now_project_repo_path'], tobranch)
    request.session['head_branch']=tobranch
    return HttpResponseRedirect(reverse('hub:code'))

def getZip(request):
    print '压缩中'
    GitFileController.mygit.zip_dir(request.session['now_project_repo_path'], 'hub/static/my-archive.zip')
    return HttpResponse('my-archive.zip')

@csrf_exempt
def code_edit(request):
    print '代码修改界面'
    file_name = request.session['now_file_name']
    with open(request.session['now_project_repo_path']+file_name,'r') as f:
        data = f.read()
    return render(request,'code_edit.html', {'data': data,'title': file_name})

def code_file(request, *args, **kwargs):
    #print args
    #file_name = (kwargs['file_name'])
    file_name = request.GET.get('file_name')
    if file_name == None: file_name = request.session['now_file_name']
    else: request.session['now_file_name']=file_name
    with open(request.session['now_project_repo_path']+file_name,'r') as f:
        data = f.read()
    return render(request, 'code_file.html', {'data': data,'title': file_name})
    #mycat_id = kwargs['pk']

def process_edit(request, *args, **kwargs):
    #print args
    #file_name = (kwargs['file_name'])
    print '处理代码修改'
    data = request.POST.get('data')
    commit_message = request.POST.get('commit_message')
    file_name = request.session['now_file_name']
    with open(request.session['now_project_repo_path']+file_name,'w') as f:
        f.write(data)
    GitFileController.mygit.change_commit(request.session['now_project_repo_path'],file_name,commit_message,request.session['user_name'],request.session['user_email'])

    description = '在项目'+request.session['now_project_name']+'中的'+request.session['head_branch']+'分支进行了注释为 "'+commit_message+'" 的提交'
    
    user_commit.record(request.session['user_name'], description)

    return HttpResponseRedirect(reverse('hub:code_file'))

def code_new(request):
    print '代码新建界面'
    return render(request,'code_new.html')

@csrf_exempt
def process_new(request, *args, **kwargs):
    #print args
    #file_name = (kwargs['file_name'])
    print '处理代码新建'
    data = request.POST.get('data')
    commit_message = request.POST.get('commit_message')
    file_name = request.POST.get('title')
    request.session['now_file_name']=file_name
    with open(request.session['now_project_repo_path']+file_name,'w') as f:
        f.write(data)
    GitFileController.mygit.change_commit(request.session['now_project_repo_path'],file_name,commit_message,request.session['user_name'],request.session['user_email'])

    description = '在项目'+request.session['now_project_name']+'中的'+request.session['head_branch']+'分支进行了注释为 "'+commit_message+'" 的提交'
    
    user_commit.record(request.session['user_name'], description)

    return HttpResponseRedirect(reverse('hub:code_file'))

@csrf_exempt
def commit(request):
    print '进入提交记录界面'
    c_list = GitFileController.mygit.log(request.session['now_project_repo_path'])
    #return render(request, 'commit.html', {'c_mes': c_mes,'c_name':c_name,'c_time':c_time,'c_len':c_len})
    return render(request, 'commit.html', {'c_list': c_list})

def branch(request):
    print '进入分支界面'

    if request.method == "POST":
        if request.POST.get('new_branch') != None:          #新建分支
            name = request.POST.get('new_branch')
            GitFileController.mygit.new_branch(request.session['now_project_repo_path'], name)
            status = 0

            msg = '在项目'+request.session['now_project_name']+'中新建了分支 '+name
            user_commit.record(request.session['user_name'], msg)

            result = "Create new branch success!"
            print(result)
        elif request.POST.get('branch_name') != None:            #删除分支
            print request.POST.get('branch_name')
            name = request.POST.get('branch_name')
            GitFileController.mygit.delete_branch(request.session['now_project_repo_path'], name)

            msg = '在项目'+request.session['now_project_name']+'中删除了分支 '+name
            user_commit.record(request.session['user_name'], msg)

            result = "Delete new branch sdsffsdf!"
            print(result)
        elif request.POST.get('frombranch') != None:        #合并分支
            msg = request.POST.get('message')
            frombranch = request.POST.get('frombranch')
            print msg
            frombranch_exist = GitFileController.mygit.merge(request.session['now_project_repo_path'],frombranch,msg)
        elif request.POST.get('tobranch') != None:          #切换分支
            tobranch = request.POST.get('tobranch')
            print tobranch
            GitFileController.mygit.switch_branch(request.session['now_project_repo_path'], tobranch)
            request.session['head_branch']=tobranch
    elif request.GET.get('branch_name') != None:            #删除分支
        print request.GET.get('branch_name')
        name = request.GET.get('branch_name')
        GitFileController.mygit.delete_branch(request.session['now_project_repo_path'], name)

        msg = '在项目'+request.session['now_project_name']+'中删除了分支 '+name
        user_commit.record(request.session['user_name'], msg)

        result = "Delete new branch success!"
        print(result)
    print 'done'
    data = GitFileController.mygit.show_branches_refs(request.session['now_project_repo_path'])
    print data
    return render(request, 'branch.html', {'data': data})



def login(request):
    print '进入登录界面'
    if request.method == 'POST':
        return process_LoginOrRegister(request)
    request.session['user_name']=None
    return render(request,'login.html')


def register(request):
    print '进入注册界面'
    if request.method == 'POST':
        return process_LoginOrRegister(request)
    return render(request,'register.html')

def profile(request):
    print ("进入主页")
    name = request.session['now_project_owner']
    if name == request.session['user_name']:
        is_user = True
    else : is_user = False

    pro_list = []

    pro_id_list = project_user.objects.filter(user_name=request.session['user_name'])
    for i, j in enumerate(pro_id_list):
        pro_list.append(Project.objects.get(pk=j.project_id))
    print (pro_list)
    print (request.session['user_name'])
    return render(request, 'projectCatalog.html', {'projects': pro_list,'is_user':is_user})
@csrf_exempt
def process_LoginOrRegister(request):
    print ("登录/注册中")
    name = request.POST.get('name')

    email = request.POST.get('email',"noemail")

    password = request.POST.get('password')

    rePassword = request.POST.get('rePassword','norepassword')

    if email != "noemail":
        try:
            user_object = models.User.objects.create(user_name=name, email=email, password=password)
        except:
            list1 = ["您使用了与别人相同的用户名！"]
            return render(request, 'register.html',{'List': json.dumps(list1)})
        GitFileController.mygit.create_dir(codehub_path+name)
    else:
        ff = models.User.objects.filter(user_name=name)
        #user_object = ff[0]
        if len(ff)!=0:user_object = ff[0]
        if len(ff)==0 or user_object.password!= password:
            print ("wrong password")
            list = ["密码或用户名错误"]
            return render(request,'login.html',{'List':json.dumps(list)})

    request.session['user_email'] = user_object.email
    request.session['user_name'] = name
    request.session['now_project_owner'] = name

    return HttpResponseRedirect(reverse('hub:profile'))



def project_create(request):
    print '创建项目'
    if request.method == 'POST':
        #dir_name是绝对路径例如/home/bob/apps/CodeHub/XYJ
        #user = request.session['user']#还要把user写入session
        #user_path = request.user.user_path
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        dir_name = codehub_path+request.session['user_name']+'/'+project_name
        repo_path = request.session['user_name']+'/'+project_name+'/'
        try:
            tem = models.Project.objects.create(project_name = project_name,description =description,repo_path = repo_path,lead_user = get_object_or_404(User, pk=request.session['user_name']))
        except:
            list = ["您在试图创建重复名字的项目！"]
            return render(request, 'projectCreate.html', {'List': json.dumps(list)})
        GitFileController.mygit.create_working_dir(dir_name, request.session['user_name'],request.session['user_email'])
        models.project_user.objects.create(project_id = tem.project_id,user_name = get_object_or_404(User, pk=request.session['user_name']))
        request.session['now_project_owner'],request.session['now_project_name'] = request.session['user_name'],project_name
        
        msg = '创建了项目 '+project_name
        user_commit.record(request.session['user_name'], msg)
        return HttpResponseRedirect(reverse('hub:code'))
    #else:
    return render(request, 'projectCreate.html')


def member(request):
#def member(request, *args, **kwargs):
    #print args

    print ('进入成员界面')
    pro_id  = request.session['now_project_id']

    input_member = request.POST.get('i_name', "ffff")
    #pro_id = 1
    print('pro_id', pro_id)
    print ('input_member', input_member)
    if len(input_member) == 0:
        pass
    else:
        ff = models.User.objects.filter(user_name=input_member)
        if len(ff) != 0:
            name = models.User.objects.get(user_name=input_member)
            pp = models.project_user.objects.filter(user_name=input_member,project_id=pro_id)
            if len(pp) == 0:
                models.project_user.objects.create(project_id=pro_id, user_name=name)
                print ('ok')

                msg = '在项目'+ request.session['now_project_name'] + u'中添加了成员 '+ str(name)
                user_commit.record(request.session['user_name'], msg)

            else:
                print ('已存在')

    all_members = models.project_user.objects.filter(project_id=pro_id)
    print (len(all_members),"#########")
    return render(request, 'member.html', {"members": all_members})

def delMem(request):
    print "删除成员"
    name = request.GET.get('member_name')
    print name
    pro_id = request.session['now_project_id']
    models.project_user.objects.filter(project_id=pro_id,user_name=name).delete()

    msg = '在项目'+request.session['now_project_name']+'中删除了成员 '+ name
    user_commit.record(request.session['user_name'], msg)

    all_members = models.project_user.objects.filter(project_id=pro_id)
    return render(request, 'member.html', {"members": all_members})
    pass

@csrf_exempt
def upload(request):
    print '上传'
    if  request.method == 'POST':
        obj = request.FILES.get('fafafa')
        f = open(os.path.join('hub','repo',request.session['now_project_owner'],request.session['now_project_name'],obj.name),'wb')
        print f
        print '@@@@@@@@@@@@@@@@'
        for line in obj.chunks():
            f.write(line)
        f.close()
        print '33333333'
        msg = '上传了'+obj.name
        GitFileController.mygit.change_commit(request.session['now_project_repo_path'],obj.name,'上传了'+obj.name,request.session['user_name'],request.session['user_email'])
        description = '在项目'+request.session['now_project_name']+'中的'+request.session['head_branch']+'分支进行了注释为 "'+msg+'" 的提交'
        
        user_commit.record(request.session['user_name'], description)
        print '********'
    return render_to_response('upload.html')


def settings(request):
    return render(request, 'settings.html')

import shutil

def delProject(request):
    print "删除项目"


    pro_id = request.session['now_project_id']
    models.project_user.objects.filter(project_id=pro_id).delete()
    models.Project.objects.filter(project_id=pro_id).delete()
    
    shutil.rmtree(request.session['now_project_repo_path'])
    msg = '删除了项目 '+request.session['now_project_name']
    user_commit.record(request.session['user_name'], msg)
    return HttpResponseRedirect(reverse('hub:profile'))

def user_record(request):

    rec_det = []
    rec = user_commit.objects.filter(user_name=request.session['user_name'])
    for i, j in enumerate(rec):
        hh = user_commit.objects.get(pk = j.commit_id)
        print hh
        rec_det.append(user_commit.objects.get(pk = j.commit_id))
    return render(request,'user_record.html',{"rec_det":rec_det})