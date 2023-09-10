class Solution:
    def sort012(self, arr, n):
        # Initialize pointers for the three partitions
        low, mid, high = 0, 0, n - 1

        # Traverse the array using the mid
        while mid <= high:
            if arr[mid] == 0:
                # If the current element is 0, swap it with the element at the low
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # If the current element is 1, move the mid one step ahead
                mid += 1
            else:
                # If the current element is 2, swap it with the element at the high
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
