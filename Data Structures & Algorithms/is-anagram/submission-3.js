class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const seen = new Map();
        for (const char of s){
            seen.set(char, ((seen.get(char)||0) + 1 ))
        }
        for(const char of t) {
            if(!seen.has(char)) return false;
            seen.set(char, ((seen.get(char)||0) - 1 ))
            if (seen.get(char) < 0) return false;
        }
        
        return true;
    }
}
