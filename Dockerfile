# استفاده از نسخه سبک پایتون
FROM python:3.9-slim

# تنظیم مسیر کاری داخل کانتینر
WORKDIR /app

# کپی کردن لیست نیازمندی‌ها و نصب آن‌ها بدون کش
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه فایل‌های پروژه (پایتون و HTML)
COPY . .

# باز گذاشتن پورت 8000 برای ارتباطات
EXPOSE 8000

# دستور اجرای سرور در زمان روشن شدن کانتینر
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]