from celery import shared_task
import requests as rq

@shared_task
def ping_self():
    try:
        rq.get('')
        print("✅ pinged self to keep render awake")
    except Exception as err:
        print(f"❌ Ping failed: {err}")