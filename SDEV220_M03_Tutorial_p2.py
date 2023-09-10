class Solution:
    def binarysearch(self, arr, n, k):
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index

            if arr[mid] == k:
                return mid  # Found k, return its position
            elif arr[mid] < k:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return -1  # Element k is not in the array
