#!/usr/bin/python


import sys
sys.path[0:0] = [
  '/home/maddalen/django_proiektu_bat/DJANGO_PROIEKTUA/src',
  '/home/maddalen/django_proiektu_bat/DJANGO_PROIEKTUA/eggs/djangorecipe-1.11-py2.7.egg',
  '/usr/local/lib/python2.7/dist-packages',
  '/home/maddalen/django_proiektu_bat/DJANGO_PROIEKTUA/eggs/zc.recipe.egg-2.0.1-py2.7.egg',
  '/home/maddalen/django_proiektu_bat/DJANGO_PROIEKTUA/eggs/zc.buildout-2.3.1-py2.7.egg',
  '/home/maddalen/django_proiektu_bat/DJANGO_PROIEKTUA',
  ]

import djangorecipe.wsgi

application = djangorecipe.wsgi.main('KULTURBIDEAK.settings', logfile='')
