<h2>1186. Maximum Subarray Sum with One Deletion</h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code>, return <i>the maximum number of unique substrings that the given string can be split into</i>.

  You can split string <code>s</code> into any list of <b>non-empty substrings</b>, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are <b>unique</b>.

A substring is a contiguous sequence of characters within a string..</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ababccc"
<strong>Output:</strong> 5
<strong>Explanation:</strong> One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> 2
<strong>Explanation:</strong> One way to split maximally is ['a', 'ba'].
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aa"
<strong>Output:</strong> 1
<strong>Explanation:</strong> It is impossible to split the string any further.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s contains only lower case English letters.</code></li>
</ul>
</div>
