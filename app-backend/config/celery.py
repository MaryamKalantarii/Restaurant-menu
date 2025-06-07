from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات Django رو به Celery معرفی می‌کنیم
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# از تنظیمات موجود در فایل settings.py استفاده می‌کنیم
app.config_from_object('django.conf:settings', namespace='CELERY')

# شغل‌ها یا task‌ها رو از اپلیکیشن‌های Django بارگذاری می‌کنیم
app.autodiscover_tasks(['config'])  # اضافه کردن نام اپلیکیشن‌ها
app.conf.worker_concurrency = 1
app.conf.worker_pool = 'solo'
