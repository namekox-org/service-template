# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import random


def generate_ip():
    return '.'.join([str(random.randint(1, 255)) for _ in range(4)])
