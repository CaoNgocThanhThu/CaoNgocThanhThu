# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:25:12 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a= float(input("Nhap a(a<>0): "))
b= float(input("Nhap b: "))
c= float(input("Nhap c: "))
delta=b**2-4*a*c
if delta <0:
    print("Phương trình vô nghiệm")
if delta >0:
    print("Phương trình có hai nghiệm phân biệt x1=",(-b + delta**0.5)/2*a, "and x2=",(-b - delta**0.5)/2*a)
if delta ==0:
    print("Phương trình có một nghiệp kép x1=x2",-b/2*a)