import schedule
import time

def run_scheduler(job_function):

    schedule.every(1).hours.do(job_function)

    while True:
        schedule.run_pending()
        time.sleep(1)
