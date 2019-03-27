# -*- coding:utf-8 -*-
'''
Created on 2018-12-06
@author xiaom
'''
import unittest
import abupy.CrawlBu.ABuXqApi as api
class Test (unittest.TestCase):

    def test_industryurl(self):
        print(api.IndustryUrl("CN", plate='保险业', page=1, level2code='J68').url)