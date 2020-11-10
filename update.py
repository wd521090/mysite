# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 12:06 下午
# @Author  : Anita
# @File    : update.py
# @Software: PyCharm

from subprocess import call

from pip._internal.utils.misc import get_installed_distributions

for dist in get_installed_distributions():
    print(dist.project_name)

for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
