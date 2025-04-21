FROM python:3.9.22-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "Todo.wsgi:application", "--bind", "0.0.0.0:8000"]