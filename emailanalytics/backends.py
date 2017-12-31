from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from emailanalytics.text_processing import replace_urls_html, replace_urls_text


chained_backend = getattr(settings,
                          'EMAIL_ANALYTICS_BACKEND',
                          'django.core.mail.backends.smtp.EmailBackend')

replace_text = getattr(settings,
                       'EMAIL_ANALYTICS_REPLACE_TXT',
                       False)


class AnalyticsEmailBackend(BaseEmailBackend):

    def __init__(self, fail_silently=False, **kwargs):
        super(AnalyticsEmailBackend, self).__init__(fail_silently)
        self.init_kwargs = kwargs

    def send_messages(self, email_messages, **kwargs):
        for msg in email_messages:
            params = {'utm_source': msg.subject,
                      'utm_medium': 'email',
                      'utm_campaign': 'webapp',
                      }

            if replace_text and msg.content_subtype == 'text':
                msg.body = replace_urls_text(msg.body, params)
            elif msg.content_subtype == 'html':
                msg.body = replace_urls_html(msg.body, params)

            if getattr(msg, 'alternatives', False):
                alts = []
                for content, mimetype in msg.alternatives:
                    if content is not None and mimetype == 'text/html':
                        content = replace_urls_html(content, params)
                alts.append((content, mimetype))
                msg.alternatives = alts

        conn = get_connection(backend=chained_backend, **self.init_kwargs)
        return conn.send_messages(email_messages)
