from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend



CHAINED_BACKEND = getattr(settings, 
                          'EMAIL_ANALYTICS_BACKEND', 
                          'django.core.mail.backends.smtp.EmailBackend')


class AnalyticsEmailBackend(BaseEmailBackend):

    def __init__(self, fail_silently=False, **kwargs):
        super(AnalyticsEmailBackend, self).__init__(fail_silently)
        self.init_kwargs = kwargs

    def send_messages(self, email_messages, **kwargs):
        for msg in email_messages:
            pass # XXX do the transform       
        
        conn = get_connection(backend=CHAINED_BACKEND, **self.init_kwargs)
        return conn.send_messages(email_messages)
            
