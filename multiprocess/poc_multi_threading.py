import multiprocessing
import concurrent.futures
import time
from typing import Callable


S_T = [4, 2, 7, 4, 3, 10, 11, 3, 2, 1]


def task(args: tuple = ('', 1)) -> str:
    name = args[0]
    sec = args[1]
    print('Task', name, 'sleeps for', sec)
    time.sleep(sec)
    return 'Task', name, sec, 'finished.'


def run_process(n: int) -> None:
    processes = [multiprocessing.Process(target=task, args=[(str(i), 1)]) for i in range(n)]
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()


def run_pool_1(n: int) -> None:
    with multiprocessing.Pool(processes=n) as pool: 
        global S_T
        # this gives us sequential execution
        # we could do task() in a for loop
        # f : is a task handle , so we need to check if it's done
        #     and retrieve the result
        # f = [pool.apply(task, [(i, S_T[i])]) for i in range(n)]
        # print(*f, sep='\n')

        # this will push task on SimpleQueue from wich processes will
        # pick tasks up
        f = [pool.apply_async(task, [(i, S_T[i])]) for i in range(n)]
        # we still hang on the longest task
        # pool.join()


        # without join the thread's will finish in background and we will
        # move forward with execution
        pool.close()
        # pool.join()

        # try to emulate doing something as soon as we get the result
        while f:
            for p in f:
                if p.ready():
                    print(p.get())
                    del f[f.index(p)]


def run_pool_2(n: int) -> None:
    with multiprocessing.Pool(processes=n) as pool:
        global S_T
        m = pool.map(task, enumerate(S_T))
        print(*m, sep='\n')
        # pool.close()
        # pool.join()

def run_executor_1(n: int) -> None:
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as exec:
        global S_T
        f = [exec.submit(task, (str(i), S_T[i])) for i in range(n)]

        # here we will hang on the longer task
        # for f1 in f:
        #     print(f1.result())

        # here we process the tasks as they finish
        for p in concurrent.futures.as_completed(f):
            print(p.result())


def run_executor_2(n: int) -> None:
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as exec:
        global S_T
        # It returns the tasks in order that they were started
        # however we still hang untill everythings done

        # Exception will be risen when retrievd value from iterator  <-- !!! -- >
        res = exec.map(task, enumerate(S_T))
        print(*res, sep='\n')


def timeme(func: Callable) -> None:
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print('Run time: ', round(end-start, 3), 'second(s)')


def main():
    print('Usage: uncomment funct to run example.')
    # run_process(10)
    # run_pool_1(10)
    # run_pool_2(10)
    # run_executor_1(10)
    # run_executor_2(10)

if __name__ == "__main__":
    timeme(main)