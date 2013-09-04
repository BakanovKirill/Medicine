### -*- coding: utf-8 -*- ####################################################
from django.core import urlresolvers
from django.conf import settings
from django import template

register = template.Library()

#Tag to render admin change link for the model
@register.inclusion_tag('change_link.html')
def edit_instance_link(instance):
    return {
        'url': urlresolvers.reverse('admin:%s_%s_change' % (
            instance._meta.app_label, instance.__class__.__name__.lower()
        ), args=([instance.pk])),
        'instance': instance
    }
