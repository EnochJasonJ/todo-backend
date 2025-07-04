from celery import shared_task
import requests as rq

@shared_task
def ping_self():
    try:
        rq.get('https://todo-backend-27zr.onrender.com/hello/')
        print("✅ pinged self to keep render awake")
    except Exception as err:
        print(f"❌ Ping failed: {err}")