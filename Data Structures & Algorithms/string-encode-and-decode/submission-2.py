class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i=j
        return res

    # ENCODE
    # Store each string in the format length#word (e.g. "3#cat")
    # Length tells decoder exactly how many characters to read
    # Join all encoded strings into one string

    # DECODE
    # Use i to track current position and j to find next '#'
    # Extract length from characters before '#'
    # Move i to start of word and j to end using length
    # Append extracted word and move i to next encoded string
    # Length-based decoding works even if words contain '#'
    