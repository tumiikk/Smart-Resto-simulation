def enqueue(queue, nama):
    queue.append(nama)


def dequeue(queue):
    if queue:
        return queue.pop(0)
    return None


def peek(queue):
    if queue:
        return queue[0]
    return None


def is_empty(queue):
    return len(queue) == 0