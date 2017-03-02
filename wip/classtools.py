# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:17:50 2016

@author: N393637
"""

class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s = %s \n' % (key, getattr(self,key)))
        return ', '.join(attrs)
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())




         