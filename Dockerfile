# استخدام صورة بايثون رسمية
FROM python:3.10-slim

# تعيين متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# إنشاء مجلد العمل
WORKDIR /app

# تثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع
COPY . .

# الأمر الافتراضي لتشغيل التطبيق
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
