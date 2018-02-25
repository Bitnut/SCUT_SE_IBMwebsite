# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import zipfile
# 创建文件夹，需要一个绝对路径作为参数
def create_dir(path):
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print '文件夹 ' + path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print '文件夹 ' + path + ' 目录已存在'
        return False

def zip_dir(start_path,file_path):
    print 'zipping'
    z = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED)
    startdir = start_path+'.'
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()