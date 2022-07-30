# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/w/weisim8h/weisim8h.beget.tech/coolsite')
sys.path.insert(1, '/home/w/weisim8h/weisim8h.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
