'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.'''


def characterReplacement( s: str, k: int) -> int:
        letters = {}
        left = 0
        maxSequence = 0
        maxDupes = 0

        for i, letter in enumerate(s):
            if letter in letters:
                letters[letter] += 1
                maxDupes = max(maxDupes, letters[letter])
            else:
                letters[letter] = 1
                maxDupes = max(maxDupes, 1)
            seq = maxDupes + k
            if i-left + 1 <= seq:
                maxSequence = max(maxSequence, i-left + 1)
            else:
                if letters[s[left]] > 1:
                    letters[s[left]] -= 1
                else:
                    letters.pop(s[left])
                left += 1
        
        return maxSequence