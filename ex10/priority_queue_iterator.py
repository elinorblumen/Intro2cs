######################################################################################
# FILE : priority_queue_iterator.py
# WRITERS : ElinorB
# EXERCISE : Intro2cs ex10
# DESCRIPTION : Priority Queues
######################################################################################



class PriorityQueueIterator:

    def __init__(self, queue):
        """
        Initiator function for the class
        :param queue: a priority queue object.
        """

        self._queue = queue
        self._pointer = queue.get_head()


    def __iter__(self):
        """
        Method returns an iterator of queue.
        """

        return self

    def __next__(self):
        """
        Method for iterating through the queue, returns next item
        in queue if such exists, otherwise returns 'Stop Iteration'.
        :return: Next task in queue
        """

        while self._pointer is not None:
            prev = self._pointer
            self._pointer = self._pointer.get_next()
            return prev.get_task()

        else:
            raise StopIteration

    def has_next(self):
        """
        Method returns True if there's another task in queue,
        and false if we've reached the end of the queue.
        """

        return self._pointer.has_next()
