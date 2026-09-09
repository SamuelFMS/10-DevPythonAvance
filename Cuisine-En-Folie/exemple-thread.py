from datetime import datetime
import threading
import time

def thread_function(name):
    print(f"{datetime.now():%H:%M:%S}: Thread {name}: starting")
    time.sleep(2)
    print(f"{datetime.now():%H:%M:%S}: Thread {name}: finishing")

if __name__ == "__main__":
    print(f"{datetime.now():%H:%M:%S}: Test")

    threads = []

    for index in range(3):
        print(f"{datetime.now():%H:%M:%S}: Main: create and start thread {index}")
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"{datetime.now():%H:%M:%S}: Main: before joining thread {index}")
        thread.join()
        print(f"{datetime.now():%H:%M:%S}: Main: thread {index} done")