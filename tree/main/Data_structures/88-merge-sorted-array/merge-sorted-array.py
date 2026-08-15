class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a,b,main_index = m-1,n-1,m+n-1

        while main_index >=0:
            if a<0:
                nums1[main_index] = nums2[b]
                b-=1
            elif b<0:
                break
            elif nums1[a] > nums2[b]:
                nums1[main_index] = nums1[a]
                a-=1
            else:
                nums1[main_index] = nums2[b]
                b-=1
            main_index -=1




        


        