class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)
        n = len(nums)
        for i in range(n):
            hmap[nums[i]].append(i)

        print(hmap)

        for key, value in hmap.items():
            diff = target - key
            if diff == key:
                if len(hmap[diff]) > 1:
                    return hmap[diff][:2]
                continue

            if diff in hmap:
                return [hmap[key][0], hmap[diff][0]]
