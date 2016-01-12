# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:20:58 2016
For file traversal.
@author: Lv
"""

import os
import os.path

def file_traversal(folderPath):
    i = 0
    for parent,dirnames,filenames in os.walk(folderPath):   #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:                          #输出文件信息
            print("filename is:", filename)
            print("last file in folder:", parent)
            print("the relpath of the file is:", os.path.join(parent,filename))
            print("the abspath of the file is:", os.path.abspath(os.path.join(parent,filename)))
            print("")
            i = i + 1
    print("该目录下总共 ", i, "个文件")

if __name__ == "__main__":
    rootdir = "../"
    file_traversal(rootdir)