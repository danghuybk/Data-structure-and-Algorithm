<h2>1402. Reducing Dishes</h2><h3>Hard</h3><hr><div><p>A chef has collected data on the <code>satisfaction</code> level of his <code>n</code> dishes. Chef can cook any dish in 1 unit of time.

<b>Like-time coefficient</b> of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  <code>time[i] * satisfaction[i]</code>.

Return the maximum sum of <b>Like-time coefficient</b> that the chef can obtain after dishes preparation.

Dishes can be prepared in <b>any</b> order and the chef can discard some dishes to get this maximum value.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> satisfaction = [-1,-8,0,5,-9]
<strong>Output:</strong> 14
<strong>Explanation:</strong> After Removing the second and last dish, the maximum total <b>Like-time coefficient</b> will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
</pre>

<p>&nbsp;</p>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> satisfaction = [4,3,2]
<strong>Output:</strong> 20
<strong>Explanation:</strong> Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
</pre>

<p>&nbsp;</p>
<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> satisfaction = [-1,-4,-5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> People don't like the dishes. No dish is prepared.
</pre>

<p>&nbsp;</p>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> satisfaction = [-2,5,-1,0,3,-3]
<strong>Output:</strong> 35
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code> n == satisfaction.length </code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>-10^3&nbsp;&lt;= satisfaction[i]&nbsp;&lt;= 10^3</code></li>
</ul>
</div>
