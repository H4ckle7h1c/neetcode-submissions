class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const frequencyMap = {};

        for (let num of nums){
            if(!frequencyMap[num]){
                frequencyMap[num] = 1;
                continue;
            }
            frequencyMap[num] += 1;
        }

        const freq = Object.entries(frequencyMap)
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .map(([key]) => key);
        console.log(freq)
        return freq;
    }
}
