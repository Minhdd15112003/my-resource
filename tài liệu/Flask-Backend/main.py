import os
from flask import request
from apscheduler.schedulers.background import BackgroundScheduler
from src import create_app
from src import cron
from threading import Lock
import logging
logging.getLogger('apscheduler').setLevel(logging.ERROR)

scheduler = None
scheduler_lock = Lock()
lock_list = [
    "/api/manager/proxy/command",
    "/api/client/proxy-restart",
    "/api/client/proxy-change-auth"
]

app = create_app()

@app.before_request
def pause_scheduler_before_request():
    with scheduler_lock:
        if request.path in lock_list and request.method != "OPTIONS":
            print("🔴 pause scheduler before request")
            # scheduler.pause_job("interfaces_update")

@app.teardown_request
def resume_scheduler_teardown_request(exception=None):
    with scheduler_lock:
        if request.path in lock_list and request.method != "OPTIONS":
            print("🟢 Resuming scheduler after request")
            # scheduler.resume_job("interfaces_update")

if __name__ == '__main__':
    
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(id='license_request', func=cron.license_request, args=(app,), trigger='interval', seconds=60, max_instances=1, coalesce=False, misfire_grace_time=5) # cứ 60 giây kiểm tra 1 lần , quá 5 giây sẽ hủy
    # scheduler.add_job(id='ddns_dynu', func=cron.ddns_dynu, args=(app,), trigger='interval', seconds=120, max_instances=1, coalesce=False, misfire_grace_time=1)
    # scheduler.start()

    app.run(debug=True, host="0.0.0.0", port=8686)

    # http_server = WSGIServer(('0.0.0.0', 80), app)
    # http_server.serve_forever()

    # try:
    #     while True:
    #         time.sleep(1)
    # except (KeyboardInterrupt, SystemExit):
    #     scheduler.shutdown()
