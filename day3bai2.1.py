# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:11:03 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a= float(input("Nhap a: "))
b= float(input("Nhap b: "))
if a== 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a==0 and b== 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Nghiệm của phương trình là:", -b/a)