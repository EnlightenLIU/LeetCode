//寻找两个有序数组的中位数
#include <stdio.h>
double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int *nums;
    int m=nums1Size;
    int n=nums2Size;
    if (m == 0)
    {
        if (n % 2 == 0)
        {
            return (nums2[n / 2 - 1] + nums2[n / 2]) / 2;
        }
        else
        {
            return nums2[n / 2];
        }
    }
    else if (n == 0)
    {
        if (m % 2 == 0)
        {
            return (nums1[m / 2 - 1] + nums1[m / 2]) / 2;
        }
        else
        {
            return nums1[m / 2];
        }
    }
    int count = 0;
    int i = 0, j = 0;
    while (count != (m * n))
    {
        if (i == m)
        {
            while (j != n)
            {
                nums[count++] = nums2[i++];
            }
            break;
        }
        if (j == n)
        {
            while (i != m)
            {
                nums[count++] = nums1[i++];
            }
            break;
        }
        if (nums1[i] < nums2[j])
        {
            nums[count++] = nums1[i++];
        }
        else
        {
            nums[count++] = nums2[i++];
        }
    }
    if (count % 2 == 0)
    {
        return (nums1[count / 2 - 1] + nums1[count / 2]) / 2;
    }
    else
    {
        return nums1[count / 2];
    }
}