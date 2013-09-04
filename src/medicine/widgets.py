from django import forms

class CalendarWidget(forms.DateInput):
    class Media:
        css = {
            'all': ('http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css',)
        }
        js = (
            'http://code.jquery.com/jquery-1.9.1.js',
              'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
            'js/utils.js'
        )