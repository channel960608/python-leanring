#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)
