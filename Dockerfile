# Sử dụng Ubuntu làm base image
FROM python:3.10

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y \
    curl gnupg apt-transport-https ca-certificates unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Cài đặt các package Python cần thiết
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code vào container
COPY . .

# Chạy server
# CMD ["gunicorn", "your_project.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]