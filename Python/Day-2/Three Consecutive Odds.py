class Solution:
    def threeConsecutiveOdds(self, arr):
        # Loop through the array up to the third-to-last element
        for i in range(len(arr) - 2):
            # Check if the current element and the next two elements are all odd
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False

# Test the function with arr = [2, 6, 4, 1]
solution = Solution()
arr = [2, 6, 4, 1]
result = solution.threeConsecutiveOdds(arr)
print(result)  # Expected output: False
