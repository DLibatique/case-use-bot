from apscheduler.schedulers.blocking import BlockingScheduler
from twee import api
from case_use_bot import generate_tweet


sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=24)
def tweet_line():
    print(generate_tweet())
    api.update_status(generate_tweet())

sched.start()
