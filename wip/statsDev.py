# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:13:06 2016

@author: n393637
"""
import numpy as np
########################################################
#Polynomial
np.polyval([0.00928,47.011,824.133], 2)  # 3 * 5**2 + 0 * 5**1 + 1
#([Polynomial, Gradient, Intercept], Yardstick)
########################################################
#Power
#Gradient * Yardstick **Intercept
print(.21456*2**0.992)
#Out[6]: 0.42674703878104975
########################################################
#Exponential
########################################################
#Log
#(log(yardstick)*Gradient)+Intercept
#(np.log(13.55)*2943.851)+9033.502
#Out[10]: 16706.315643731341
########################################################
#Power
#np.exp(Intercept)*(Yardstick**Gradient)
#np.exp(8.168788)*6.5**0.569245
#Out[11]: 10242.510455235091





