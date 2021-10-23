#crummy.com/software/BeautifulSoup/bs4/doc
#schedule.readthedocs.io/en/stable
#uptimerobot.com

import time
import schedule
import website
from replit import db

import basic
import hchs
import hgsh

website.alive() #for uptimerobot

send_email: bool = False
run_immediate: bool = False


#for testing
#db["hchs_latest_date"] = "2021-10-10"
#db["hchs_latest_title"] = "Test title"
#db["hgsh_latest_id"] = "10499"


def ShowResult(result: list):
  for re in result:
    print(re.detail())
    print()


def Job():
  if(send_email):
    basic.push_email("hchs", hchs.get_news())
  else:
    ShowResult(hchs.get_news())
  #WIP


def ScheduleRun():
  #replit uses UTC+0, so schedule the tasks 8 hours earlier, using 24-hour clock
  scheduler: schedule.Scheduler = schedule.Scheduler()

  time_to_send: str = "10:00"

  scheduler.every().monday.at(time_to_send).do(Job)
  #scheduler.every().tuesday.at(time_to_send).do(Job)
  #scheduler.every().wednesday.at(time_to_send).do(Job)
  scheduler.every().thursday.at(time_to_send).do(Job)
  #scheduler.every().friday.at(time_to_send).do(Job)

  print("tasks scheduled")

  while True:
    scheduler.run_pending()
    time.sleep(1)


if(run_immediate):
  Job()

ScheduleRun()