//寻找两个有序数组的中位数
#include <stdio.h>
double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int *nums;
    if(nums1Size==0)
    {
        if(nums2Size%2==0)
        {
            return (nums2[nums2Size/2-1]+nums2[nums2Size/2])/2;
        }
        else
        {
            return nums2[nums2Size/2];
        }
    }
    else if(nums2Size==0)
    {
        if (nums1Size % 2 == 0)
        {
            return (nums1[nums1Size / 2 - 1] + nums1[nums1Size / 2]) / 2;
        }
        else
        {
            return nums1[nums1Size / 2];
        }
    }
    
}