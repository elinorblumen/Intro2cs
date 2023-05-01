######################################################################################
# FILE : node.py
# WRITERS : ElinorB
# EXERCISE : Intro2cs ex10 
# DESCRIPTION : Priority Queues
######################################################################################




class Node:

    def __init__(self, task, next=None):
        """
        Initiator of class node.
        :param task: Nodes task
        :param next: Nodes next
        """

        self._task = task
        self._next = next



    def get_priority(self):
        """
        Getter for nodes task priority.
        """

        return self._task.get_priority()



    def set_priority(self, new_priority):
        """
        Setter for nodes task priority.
        :param new_priority: New priority to be implemented
        """

        self._task.set_priority(new_priority)



    def get_task(self):
        """
        Getter for nodes task.
        :return: Node task
        """

        return self._task



    def get_next(self):
        """
        Getter for nodes 'next'.
        """

        return self._next



    def set_next(self, next_node):
        """
        Setter for node next.
        :param next_node: New next node to be implemented
        """

        self._next = next_node



    def has_next(self):
        """
        Method checks whether node has next.
        :return: True iff node has 'next'
        """

        if self._next is not None:
            return True

        else:
            return False
