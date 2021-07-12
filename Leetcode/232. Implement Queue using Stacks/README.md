<h2>232. Implement Queue using Stacks</h2><h3>Hard</h3><hr><div><p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).

Implement the <code>MyQueue</code> class:

- <code>void push(int x)</code> Pushes element x to the back of the queue.
- <code>int pop()</code> Removes the element from the front of the queue and returns it.
- <code>int peek()</code> Returns the element at the front of the queue.
- <code>boolean empty()</code> Returns true if the queue is empty, false otherwise.
Notes:

  You must use <b>only</b> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
  Follow-up: Can you implement the queue such that each operation is <b>amortized</b> O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> ["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output:</strong> [null, null, null, 1, 1, false]
<strong>Explanation:</strong> MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
  <li><code>At most 100 calls will be made to push, pop, peek, and empty.</code></li>
  <li><code>All the calls to pop and peek are valid.</code></li>
</ul>
</div>
