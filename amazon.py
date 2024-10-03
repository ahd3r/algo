'''
Some developers at Amazon are building a prototype for a simple rate-limiting algorithm. There are n requests to be processed by the server represented by a string requests where the ith character represents the region of the ith client. Each request takes 1 unit of time to process. There must be a minimum time gap of minGap units between any two requests from the same region.

The requests can be sent in any order and there can be gaps in transmission for testing purposes. Find the minimum amount of time required to process all the requests such that no request is denied.

Example
Suppose n = 6, requests = "aaabbb" and minGap = 2.

The requests can be sent in the order "ab_ab_ab", where "_" represents that no request was sent. Here, the minimum time gap between two requests from the same region is minGap = 2. The total time taken is 8 units.

Function Description:
Complete the function getMinTime in the editor below.

getMinTime has the following parameters:

int n: the number of requests
string requests: the regions of requests to be processed
int minGap: the minimum gap between requests from the same region
Returns:

int: the minimum time required to process all the requests
Constraints:

1 ≤ length of requests ≤ 10^5
0 ≤ minGap ≤ 100
It is guaranteed that requests contain lowercase English characters only.
Sample Input for Custom Testing:

STDIN   FUNCTION
5       -> PnL[] size n = 4
1       -> PnL = [1, 1, 1, 1]
1
1
1
1
Sample Output:
2

Explanation:
There are multiple possible PnLs such as [1, -1, -1, 1], [-1, 1, -1, 1], [-1, 1, 1, -1], etc. However, it is optimal to modify the PnL to be [1, 1, -1, 1, -1] or [1, 1, -1, -1, 1].
'''

def getMinTime(requests, minGap):
    len_reqs = [1]
    sorted_reqs = sorted(requests)
    for i in range(1, len(sorted_reqs)):
        if sorted_reqs[i] == sorted_reqs[i-1]:
            len_reqs[-1] += 1
        else:
            len_reqs.append(1)
    len_reqs.sort(reverse=True)

    empty_space_arr = (len_reqs[0] - 1) * [minGap]
    res = len_reqs[0] + (len_reqs[0] - 1) * minGap
    for len_req in len_reqs[1:]:
        while len_req != 0:
            start_point = None
            for empty_space_el_i in range(len(empty_space_arr)):
                if empty_space_arr[empty_space_el_i] != 0:
                    if start_point is None:
                        start_point = empty_space_arr[empty_space_el_i]
                    empty_space_arr[empty_space_el_i] -= 1
                    len_req -= 1
                    break
            if len_req != 0:
                if start_point == None:
                    empty_space_arr += (len_req - 1) * [minGap]
                    res += len_req + (len_req - 1) * minGap
                else:
                    res += (minGap - start_point - 1) + (minGap + 1) * len_req
                    empty_space_arr += [minGap - start_point - 1 - 1] + len_req * [minGap]
                break
    return res

'''
Developers at Amazon are working on a text generation utility for one of their new products.

Currently, the utility generates only special strings. A string is special if there are no matching adjacent characters. Given a string s of length n, generate a special string of length n that is lexicographically greater than s. If multiple such special strings are possible, then return the lexicographically smallest string among them.

Notes:
- Special String: A string is a special if there are no two adjacent characters that are the same.
- Lexicographical Order: This is a generalization of the way words are alphabetically ordered in dictionaries: For example, 'abc' is lexicographically smaller than 'abd', because 'c' comes before 'd' in alphabet

A string a is lexicographically smaller than a string b if and only if one of the following holds:
- a is a prefix of b, but a is not equal to b. For example, 'abc' is smaller than 'abcd'
- In the first position where a and b differ, the character in a comes before the character b  in the alphabet. For example, 'abc' is smaller than 'abd' because 'c' comes before 'd'.

Important Considerations:
- If the character is 'z', it is the last character in the alphabet and cannot be increased futher. The string should not wrap around to 'a' after 'z'
- The output string must not have ant adjacent characters that are the same

Example:
Suppose s = 'abbd'
Some of the special strings that are lexicographically greater than s are shown.

     -> abda
abbd -> abcd
     -> abca (amazon's)
     -> abcd

The lexicographically smallest special string that is grater 'abbd' is 'abca'.

Fuction Description
Complete the function getSpecialString in the editor below.

getSpecialString has the following parameter:
    s: the input string

Returns
    string: the lexicographically smallest string that is greater that is greater than s.
If no such special string exists, return '-1'.

Constraints:
- 1 <= s <= 10^6
- s consists of lowercase English letters only

Sample case:
- abccde -> abcdab
- zzab -> -1 (explanation - there is no special string of length 4 that is lexicographically greater than s.)
'''

def getSpecialString(s):
    alph_string = 'abcdefghijklmnopqrstuvwxyz'
    res = ""
    s_special = True
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            if s[i] == 'z':
                return '-1'
            s_special = False
            res += alph_string[alph_string.index(s[i]) + 1]
            break
        else:
            res += s[i]
    if s_special:
        return s
    while len(res) < len(s):
        if res[-1] == 'a':
            res += 'b'
        else:
            res += 'a'
    return res

print(getSpecialString("abccde"))
print(getSpecialString("zzab"))
print(getSpecialString("abbd"))
