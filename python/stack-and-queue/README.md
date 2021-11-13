# Stacks and Queues

**Stacks**:
A stack is an array or list structure of function calls and parameters used in modern computer programming and CPU architecture. Similar to a stack of plates at a buffet restaurant or cafeteria, elements in a stack are added or removed from the top of the stack, in a “last in first, first out” or LIFO order

**Queues**:

A queue is a first-in first-out (FIFO) abstract data type that is heavily used in computing. Uses for queues involve anything where you want things to happen in the order that they were called, but where the computer can't keep up to speed

## Challenge
<!-- Description of the challenge -->
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
**Stacks**:

- Stacks push ▶ O(1)
- Stacks pop ▶ O(1)
- Stacks peek ▶ O(1)
- Stacks is_empty ▶ O(1)

**Queues**:

- Queues dequeue ▶ O(1)
- Queues enqueue ▶ O(1)
- Queues peek ▶ O(1)
- Queues is_empty ▶ O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

### My stack class has 4 methods:

- `pop()` this method removes the item on top of the stack by setting its pointer to self.top.next. I also store a reference to the value to be popped in a temp variable, so that it can be returned

- `push()` pushes a new node onto the stack by setting the current top node as the incoming node's next, then setting the new node as self.top This method takes in a single value as its only parameter

- `peek()` returns the value at the top of the stack, if it exists

- `is_empty()` if self.top exists and returns a boolean

#### My Queue class has 4 similar methods:

enqueue() Appends a node to the end of the queue by pointing the current rear (if it exists) to the new node, and assigning self.rear to the new node. If the queue is empty, we assign the new_node to both the front and the rear.

dequeue() removes a node from the front of the queue, if the queue is empty, we print a message and return the empty queue To remove the first node, we first store a reference to it in a temp variable We then reassign self.front to be the next item in the queue The return is a string of the value of the temp variable

is_empty() Checks if self.front exists and returns a boolean

## Code

[stack](./stack_and_queue/stack.py)

[queue](./stack_and_queue/queue.py)

## Testing

- [x] Can successfully push onto a stack
- [x] Can successfully push multiple values onto a stack
- [x] Can successfully pop off the stack
- [x] Can successfully empty a stack after multiple pops
- [x] Can successfully peek the next item on the stack
- [x] Can successfully instantiate an empty stack
- [x] Calling pop or peek on empty stack raises exception
- [x] Can successfully enqueue into a queue
- [x] Can successfully enqueue multiple values into a queue
- [x] Can successfully dequeue out of a queue the expected value
- [x] Can successfully peek into a queue, seeing the expected value
- [x] Can successfully empty a queue after multiple dequeues
- [x] Can successfully instantiate an empty queue
- [x] Calling dequeue or peek on empty queue raises exception