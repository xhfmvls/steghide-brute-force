from threading import Thread, Lock, current_thread
from queue import Queue
import time
import os

filename = 'Invitation Card.jpg'

def load_word_list(wordlist_filename):
    print('[*] Loading wordlist')
    with open(wordlist_filename) as wordlist_file:
        for word in wordlist_file:
            wordlist.put(word[:-1])
            pass

def brute(wordlist, lock):
    while not wordlist.empty(): 
        word = wordlist.get()
        with lock:
            print('[*]', current_thread().name, word)
            os.system(f'steghide extract -sf {filename} -p {word}')
        wordlist.task_done()

if __name__ == '__main__':
    start_time = time.time()

    wordlist = Queue()
    load_word_list('wordlist/testing.txt') # you may change this value
    threads_num = 100 # you may change this value
    lock = Lock()
    
    for x in range(threads_num): 
        thread = Thread(name=str(x + 1), target=brute, args=(wordlist, lock))
        thread.daemon = True # dies when the main thread dies
        thread.start()

    wordlist.join()

    finished_time = time.time()
    print('[*] END')
    print('[*] Time needed {}'.format(finished_time - start_time))