from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    if isinstance(value, str):
        try:
            date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return value  
    elif isinstance(value, datetime):
        date_obj = value
    else:
        return value  
    
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")