import time


def countdown():
    k = input("Enter the time(in seconds) : ")
    t=int(k)
    while t>=0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t =t - 1
    countdown()

countdown()