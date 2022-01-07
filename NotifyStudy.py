import schedule
import time
from win10toast import ToastNotifier
toaster=ToastNotifier()

def test():
    toaster.show_toast("Notification","มีเรียน 8:20",duration=10)

def test1():
    toaster.show_toast("Notification","มีเรียน 9:10",duration=10)

def test2():
    toaster.show_toast("Notification","นอนได้เเล้วไอหน้าโง่",duration=10)

#Time
schedule.every().day.at("20:55").do(test2)

while True:
    schedule.run_pending()
    time.sleep(1)