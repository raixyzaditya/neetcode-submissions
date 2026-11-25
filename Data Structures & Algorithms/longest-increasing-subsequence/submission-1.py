class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        l = len(nums)
        for i in range(1,l):
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                
                j = len(arr)-1
                idx = j
                while j > -1:
                    if arr[j] >= nums[i]:
                        idx = j
                    else:
                        break
                    j -= 1
                arr[idx] = nums[i]
        return len(arr)

        