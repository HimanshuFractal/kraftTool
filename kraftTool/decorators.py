# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:00:24 2022

@author: C039741
"""

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance