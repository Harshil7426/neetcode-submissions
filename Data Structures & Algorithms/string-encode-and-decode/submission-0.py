class Solution:
    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Length of the next string
            length = int(s[i:j])

            # Start of actual string
            start = j + 1

            # Extract exactly 'length' characters
            result.append(s[start:start + length])

            # Move to the next encoded string
            i = start + length

        return result
