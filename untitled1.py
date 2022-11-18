# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:34:14 2022

@author: henry
"""

import logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s : %(message)s',filename='mylog.txt') 

logging.debug("debug message") 


logging.shutdown()
