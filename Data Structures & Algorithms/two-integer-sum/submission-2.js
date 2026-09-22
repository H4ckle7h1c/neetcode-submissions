class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = new Map();
        for (let i = 0; i < nums.length; i++) {
            const n = nums[i];
            const complement = target - n;

            if (seen.has(complement)) {
                return [seen.get(complement), i];
            }

            seen.set(n, i);
    
        }}
}
