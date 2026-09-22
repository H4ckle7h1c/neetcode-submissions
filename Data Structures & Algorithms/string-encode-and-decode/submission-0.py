class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in range(len(strs)):
            encoded.append(f'{len(strs[s])}#{strs[s]}')
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0
        while i < len(s):
            start = s.find('#',i)
            word_length = int(s[i:start])
            word = s[start+1:start+1+word_length]
            i=start+word_length+1
            decoded.append(word)
        return decoded
