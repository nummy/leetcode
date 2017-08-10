"""
Description: Write a function to find the longest common prefix string amongst an array of strings.
Date: 2017.08-10 17:15
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_length = len(strs[0])
        for elem in strs:
            if len(elem) < min_length:
                min_length = len(elem)
        if min_length == 0:
            return ""
        res = ""
        for i in range(1, min_length+1):
            prefix = strs[0][:i]
            flag = False
            for elem in strs:
                if elem[:i] != prefix:
                    flag = True
                    break
            if flag:
                break
            else:
                res = prefix
        return res

if __name__ == "__main__":
    s = Solution()
    strs = ["about", "abuse", "abx"]
    print s.longestCommonPrefix(strs)