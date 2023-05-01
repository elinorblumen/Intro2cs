######################################################################################
# FILE : priority_queue.py
# WRITERS : ElinorB
# EXERCISE : Intro2cs ex10
# DESCRIPTION : Priority Queues
######################################################################################


from node import Node
from priority_queue_iterator import PriorityQueueIterator


class PriorityQueue:


    def __init__(self, tasks = []):
        self._head = None
        self._tasks = tasks
        self._length = 0
        self._pointer = self._head
        for task in self._tasks:
            self.enque(task)



    def enque(self, task):
        """
        Method for adding a task to queue with respect to its priority.
        :param task: New task to be added
        """

        task_priority = task.get_priority()
        prev = None
        curr = self._head
        while curr and curr.get_priority() >= task_priority:
            prev = curr
            curr = curr.get_next()

        task_node = Node(task, curr)
        if prev is None:
            self._head = task_node
        else:
            prev.set_next(task_node)
        self._length += 1




    def peek(self):
        """
        Method returns head task
        :return: Head task
        """
        if self._head is None:
            return None

        else:
            return self._head.get_task()


    def deque(self):
        """
        Method returns the task in the head of our queue and deletes the task from the queue.
        (returns None if our queue is empty).
        :return: Task in the head of our queue
        """

        if self._head is None:
            return None

        else:
            self._length -= 1
            prev = self._head
            curr = self._head.get_next()
            self._head = curr
            return prev.get_task()


    def get_head(self):
        """
        Returns the node object which is our queue head.
        :return: Head of queue
        """

        return self._head


    def change_priority(self, old, new):
        """
        Method for changing the first task in queue with specific priority to have a different
        priority and different location in queue due to it.
        :param old: Old priority
        :param new: New priority
        :return: None if there's no such task
        """


        if self.find_node_by_priority(old) != 0:
            curr = self.find_node_by_priority(old)
            prev = self.find_prev(curr)

            if curr.has_next:
                prev.set_next(curr.get_next())

            curr.set_priority(new)
            new_task = curr.get_task()
            self.enque(new_task)

        else:
            return



    def find_node_by_priority(self, priority):
        """
        Method returns the first node in the queue with specific priority,
        returns False if no such node exists.
        :param priority: Priority to be searched for
        :return: First node in queue with same priority
        """

        prev = self._head


        while prev and prev.get_priority() > priority:
                if prev.has_next():
                    prev = prev.get_next()
                else:
                    return False

        if prev and prev.get_priority() == priority:
            return prev

        else:
            return False


    def find_prev(self, node):
        """
        Method returns the node previous to specific given node. returns None if there's
        no previous node.
        :param node: Given node
        :return: Node previous to given node if such exists
        """

        if node is self._head:
            return None

        else:

            node_by_priority = self._head

            while True:
                if node_by_priority is node:
                    return prev

                elif node_by_priority.has_next():
                    prev = node_by_priority
                    node_by_priority = node_by_priority.get_next()

                else:
                    return None



    def __len__(self):
        """
        Method returns queue length
        """

        return self._length


    def __iter__(self):
        """
        Method returns an iterator over our queue
        """

        return PriorityQueueIterator(self)


    def __next__(self):
        """
        Method for iterating through the queue, returns next item
        in queue if such exists, otherwise returns 'Stop Iteration'.
        :return: Next task in queue
        """

        if self._pointer.has_next():
            prev = self._pointer
            self._pointer = self._pointer.get_next()
            return prev.get_task()

        else:
            raise StopIteration


    def __str__(self):
        """
        Method returns string representation of our queue.
        """

        queue_str_task = []
        node = self._head

        while node:
            task = node.get_task()
            node = node.get_next()
            queue_str_task.append(task)

        return str(queue_str_task)


    def __add__(self, other):
        """
        Method receives another queue and joins two queues together.
        :param other: Another queue
        :return: One queue made from the two joined together
        """

        new_list = PriorityQueue()
        curr_self = self._head
        curr_other = None

        while curr_self:
            new_list.enque(curr_self.get_task())
            curr_self = curr_self.get_next()
            curr_other = other._head

        while curr_other:
            new_list.enque(curr_other.get_task())
            curr_other = curr_other.get_next()

        return new_list

    def __eq__(self, other):
        """
        Method receives another queue and checks whether the two queues have same tasks with
        same priority.
        :param other: Another queue
        :return: True if two queues are identical, False otherwise
        """

        if len(self) != len(other):
            return False
        curr_self = self._head
        curr_other = other._head
        while curr_self and curr_other:
            if curr_self.get_task() != curr_other.get_task():
                return False
            curr_self = curr_self.get_next()
            curr_other = curr_other.get_next()
        return True












