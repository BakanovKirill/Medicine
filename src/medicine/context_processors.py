### -*- coding: utf-8 -*- ####################################################

from django.conf import LazySettings


def settings(request):
    dict_settings = dict()
    settings = LazySettings()
    #Good hack to use pdb-friendly dir function
    for k in dir(settings):
        #Wrap settings as object
        attr = getattr(settings._wrapped, k)
        if not callable(attr) and k.isupper() and not k.startswith('_'):
            dict_settings[k] = attr
    return dict_settings
