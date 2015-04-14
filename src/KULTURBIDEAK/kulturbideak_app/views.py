# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.forms.formsets import formset_factory
from django.utils.translation import ugettext as _,get_language
from itertools import islice, chain
from django.utils import simplejson
from django.template import Context, Template
from django.contrib.auth.decorators import user_passes_test

from utils import *
from django.core.paginator import Paginator

from django.views.decorators.cache import cache_page

