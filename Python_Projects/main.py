import schedule
import time
from jkdownloader_script import check_jdownloader


schedule.every(2).minutes.do(check_jdownloader)

counter = 1
while True:
    schedule.run_pending()
    if counter % 60 == 0:
        print(counter)
    if counter > 120:
        counter = 0
    time.sleep(1)
    counter += 1