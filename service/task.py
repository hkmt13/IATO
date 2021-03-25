from IATOPRO.celery import app
from celery.schedules import crontab

@app.task
def hellowrld():
    print("djfdhdf")


app.conf.beat_schedule = {
 "run-me-every-ten-seconds": {
 "task":  'tasks.add',
        'schedule': crontab( minute=30),
        'args': (16, 16),
 }
}


