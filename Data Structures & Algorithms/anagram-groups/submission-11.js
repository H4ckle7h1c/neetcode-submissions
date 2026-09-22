class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        if(strs.length === 1) return [strs]

        const lettersFrequencyMap = {};

        for (const str of strs) {
            const freqArray = new Array(26).fill(0);
            for (const char of str) {
                const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
                freqArray[idx] = (freqArray[idx] || 0) + 1;
                console.log(idx,char)
            }
            const key = freqArray.join('|');
            if (!lettersFrequencyMap[key]) {
                lettersFrequencyMap[key] = [];
            }
            lettersFrequencyMap[key].push(str)
        }
        console.log(lettersFrequencyMap)
        return Object.values(lettersFrequencyMap)
    }
}
