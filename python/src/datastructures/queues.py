"""
Queue data structure implementation module.

This module provides implementation and use case of Queue data structure with basic operations:

A queue follows the First-In-First-Out (FIFO) principle, where the first element added
is the first one to be removed. It is similar to a queue of people in a waiting line.


"""

from queue import Queue
from threading import Thread
from time import sleep
import logging

_SLEEP_DURATION = 0.5


def place_order(orders: list[str], queue: Queue) -> None:
    """
    This places an order by inserting that into a queue every 0.5 second.
    Args:
        orders (List[str]): List of order items to place.
        queue (Queue): Queue to place order.
    Returns:
        None
    """
    for order in orders:
        queue.put(order)
        sleep(_SLEEP_DURATION)


def server_order(queue: Queue) -> None:
    """
    Server by retrieving items in a queue every 0.5 second.
    Args:
        queue (Queue): Queue containing list of order items.
    """
    while not queue.empty():
        logging.warning(queue.get())
        sleep(_SLEEP_DURATION)


def ordering_system():
    """
    Design a food ordering system where your python program will run two threads.
     -  Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint use time.sleep(0.5) function).
     - Serve Order: This thread will serve the order: All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
     - Pass the following list as an argument to place order thread:
            orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
    Returns:

    """
    queue = Queue()
    orders = ["pizza", "samosa", "biryani", "burger"]
    thread1 = Thread(
        target=place_order,
        args=(
            orders,
            queue,
        ),
    )
    thread2 = Thread(target=server_order, args=(queue,))
    thread1.start()
    sleep(_SLEEP_DURATION)
    thread2.start()
