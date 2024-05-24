class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Initialize the resulting array 'arr'
        arr = []
        
        # Sort the 'nums' array to easily pick the minimum elements
        nums.sort()
        
        # Loop until 'nums' is empty
        while nums:
            # Alice removes the minimum element (first element after sorting)
            alice_pick = nums.pop(0)
            # Bob removes the new minimum element (first element after Alice's pick)
            bob_pick = nums.pop(0)
            
            # First Bob appends his pick to 'arr', then Alice does the same
            arr.append(bob_pick)
            arr.append(alice_pick)
        
        return arr
