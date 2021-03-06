<h2>1402. Reducing Dishes</h2><h3>Hard</h3><hr><div><p>You are given an <code>m * n</code> matrix, mat, and an integer <code>k</code>, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth <b>smallest</b> array sum among all possible arrays.</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> mat = [[1,3,11],[2,4,6]], k = 5
<strong>Output:</strong> 7
<strong>Explanation:</strong> Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> [[1,3,11],[2,4,6]], k = 9
<strong>Output:</strong> 17
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> [[1,10,10],[1,4,5],[2,3,6]], k = 7
<strong>Output:</strong> 9
<strong>Explanation:</strong> Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> [[1,1,10],[2,2,9]], k = 7
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code> m == mat.length </code></li>
	<li><code> n == mat.length[i] </code></li>
	<li><code>1 &lt;= m, n &lt;= 40</code></li>
  <li><code>1 &lt;= k &lt;= min(200, n ^ m)</code></li>
	<li><code>mat[i] is a non decreasing array.</code></li>
</ul>
</div>
