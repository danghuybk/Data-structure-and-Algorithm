<h2>205D. Kth Excludedg</h2><h3>Score 400</h3><hr><div><p>
You are given a sequence of N positive integers: <code>A = (A1, A2,…, AN)</code>, and Q queries.

In the i-th query (1 &lt;= i &lt;= Q), given a positive integer Ki, find the Ki-th smallest integer among the positive integers that differ from all of <code>A1, A2,…, AN.</code>
</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= N, Q &lt;= 10^5</code></li>
  <li><code>1 &lt;= A1 &lt;A2 &lt; ... &lt; AN &lt;= 10^18</code></li>
	<li><code>1 &lt;= Ki &lt;= 10^18</code></li>
</ul>  

<p><strong>Input</strong></p>
Input is given from Standard Input in the following format:
<pre>N, Q
A1 A2 ... AN
K1
K2
KN</pre>

<p><strong>Output</strong></p>
Print Q lines. The i-th line should contain the response to the i-th query.
<p>&nbsp;</p>
<p><strong>Sample input 1:</strong></p>
<pre>4 3
3 5 6 7
2
5
3</pre>
<p><strong>Sample output 1:</strong></p>
<pre>2
9
4</pre>

<p><strong>Sample input 2:</strong></p>
<pre>5 2
1 2 3 4 5
1
10</pre>

<p><strong>Sample output 2:</strong></p>
<pre>6
15</pre>

</div>

