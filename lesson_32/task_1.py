"""
Make a class called Counter, and make it a subclass of the Thread class in the Threading module. Make the class
have two global variables, one called counter set to 0, and another called rounds set to 100.000. Now implement the
run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and for each time
increments the value of the counter by 1. Create 2 instances of the thread and start them, then join them and check
the result of the counter, it should be 200.000, right? Run it a couple of times and consider some different reasons
why you get the answer that you get.
"""
import threading


class Counter:

    def __init__(self):
        self.counter = 0
        self.rounds = 100000

    def run(self, lock):
        for _ in range(self.rounds):
            lock.acquire()
            self.counter += 1
            lock.release()


def main_task(counter: Counter):
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=counter.run, args=(lock,))
    t2 = threading.Thread(target=counter.run, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('Finished')


if __name__ == "__main__":
    counter = Counter()
    main_task(counter)
    print(counter.counter)
