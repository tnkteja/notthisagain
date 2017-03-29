[1] while this shows several solutions. The popular ones are using two stacks yes, but clearing the first stack for every time we have need for dequeing an element, into the other stack. Clearly we see that it si not efficient whn every other operation is deque.

* For each enqueue we are pushing, but for every deque we are poping and pushing and poping, with condition that at the time to deque the other stack is not empty.

Just for the sanity. Oh god why the hell do you have to pop and push on to other stack. why can't you just copy the wholething iterating in reverse and initialise on the new stack. 

## References
1. _http://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks_