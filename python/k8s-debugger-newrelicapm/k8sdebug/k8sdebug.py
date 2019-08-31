#!/usr/bin/env python3

import requests, os, json, sys, time
from datetime import datetime
import newrelic.agent

target_url = os.environ.get('target_url')
sleep_seconds = os.environ.get('sleep_seconds')
request_amount = os.environ.get('request_amount')

@newrelic.agent.background_task()
def http_call():
    x = requests.get(target_url)
    return x.text 

print("debug env", target_url, sleep_seconds, request_amount)

while True:
    counter = int(request_amount)

    while counter >= 0:
        counter -= 1
        print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], http_call())

    print("sleep", sleep_seconds)
    time.sleep(int(sleep_seconds))
       