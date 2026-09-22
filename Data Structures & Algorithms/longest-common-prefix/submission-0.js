class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */

    longestCommonPrefix(strs) {
        let root = { children: {}};
        for (const str of strs) {
            let currNode = root;
            for (const char of str){
                const exists = currNode.children[char];
                if(exists){
                    currNode = exists;
                    continue;
                }
                currNode.children[char] = { children: {}};
                currNode = currNode.children[char]
            }
            currNode.isEnd = true;
        }
    
        let longestPrefix = [];
        let currNode = root;
        while (true) {
            const keys = Object.keys(currNode.children);
            if (keys.length !== 1 || currNode.isEnd) break;

            const char = keys[0];
            longestPrefix.push(char);
            currNode = currNode.children[char];
        }
        return longestPrefix.join('');
    }
}
