<h2>1535C. Unstable String</h2><h3>Rating 1400</h3><hr><div><p>
You are given a string s consisting of the characters 0, 1, and ?.

Let's call a string <b>unstable</b> if it consists of the characters 0 and 1 and any two adjacent characters are different (i. e. it has the form 010101... or 101010...).

Let's call a string <b>beautiful</b> if it consists of the characters 0, 1, and ?, and you can replace the characters ? to 0 or 1 (for each character, the choice is independent), so that the string becomes <b>unstable</b>.

For example, the strings 0??10, 0, and ??? are beautiful, and the strings 00 and ?1??1 are not.

Calculate the number of beautiful contiguous substrings of the string s.  
</p>
<p><strong>Input</strong></p>
The first line contains a single integer t (1 &lt;= t &lt;= 10^4) — number of test cases.

The first and only line of each test case contains the string s (1 &lt;= |s| &lt;= 2⋅10^5) consisting of characters 0, 1, and ?.

It is guaranteed that the sum of the string lengths over all test cases does not exceed 2⋅10^5.

<p><strong>Output</strong></p>
For each test case, output a single integer — the number of beautiful substrings of the string s.  
  
<p>&nbsp;</p>
<p><strong>Example:</strong></p>
<pre><strong>Input:</strong> 
3
0?10
???
?10??1100
<strong>Output:</strong>
8
6
25
</pre>
</div>
