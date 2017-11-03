#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time

import os, time

while True:
    return1 = os.system('ping 114.114.114.114 -c 4')  # check wifi connection
    if return1:
        print('******wifi is down, restrart…***\n')
        os.system('sudo ifup wlan0')

    time.sleep(5 * 60)  # 5 minutes
