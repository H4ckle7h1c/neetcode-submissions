class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        const freq = new Array(nums.length+1).fill();
        
        for(let num of nums){
            count[num] = 1 + (count[num] || 0);
        }
        Object.entries(count).forEach((kv) => {
            if (!freq[kv[1]]){
                freq[kv[1]]=[kv[0]];
                return;
            }
            freq[kv[1]].push(kv[0]);
        })
        const res = [];
        for (let i = freq.length - 1; i > 0; i--) {
            if (!freq[i]) continue;

            for (const v of freq[i]) {
                if (res.length === k) return res;
                res.push(v);
            }
        }
        return res;
    }
}
