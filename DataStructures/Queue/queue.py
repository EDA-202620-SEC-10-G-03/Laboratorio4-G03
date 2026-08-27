from DataStructures.List import single_linked_list as sll

def new_queue():
    queue = sll.new_list()
    return queue

def enqueue(my_queue, element):
    my_queue = sll.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    if sll.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        elemento = sll.remove_first(my_queue)
        return elemento

def peek(my_queue):
    if sll.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return sll.first_element(my_queue)


def is_empty(my_queue):
    return sll.is_empty(my_queue)


def size(my_queue):
    return sll.size(my_queue)