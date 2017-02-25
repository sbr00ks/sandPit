#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:50:38 2017

@author: simon
"""
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

import quandl, pandas as pd
quandl.ApiConfig.api_key = ''
mydata = quandl.get("EIA/PET_RWTC_D",returns="pandas")

# In[]

mydata=quandl.get("CVR/ANGEL_SECTORS", authtoken="",returns="pandas")
mydata.plot()
