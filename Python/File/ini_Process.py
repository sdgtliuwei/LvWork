# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:38:58 2016
For .ini file process. more information : .ini file need with format : UTF-8 without BOM
@author : sdgtliuwei
version : Python 3.4
"""

import configparser

"""读取ini文件"""
config = configparser.ConfigParser()
config.read("Test.ini")
sections = config.sections()
for i in sections:
    print(i)
sections.clear()
name = config.get("section1","name")
print(name)
config.clear()

"""创建ini文件"""
try:
    config.add_section("Province")
    config.set("Province","name","shandong")
    config.set("Province","nmber","1")
except configparser.DuplicateSectionError:
    print("Section 'Province' already exists")    
try:
    config.add_section("School")
    config.set("School","name","ouc")
    config.set("School","address","qd")  
except configparser.DuplicateSectionError:
    print("Section 'School' already exists")
config.write(open("test_w.ini", "w")) 
config.clear()

"""修改ini文件"""
config.read("Test.ini")
config.set("section2", "password", "p22")
config.remove_section("section1")
config.remove_option("section2", "name")
config.write(open("Test.ini", "w")) 
config.clear()