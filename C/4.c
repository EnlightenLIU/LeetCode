//寻找两个有序数组的中位数
#include <stdio.h>
double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    //int *nums;

    int m = nums1Size;
    int n = nums2Size;
}

void main()
{
    int a[4] = {1, 3, 5, 7};
    int b[4] = {2, 4, 6, 8};
    double c;
    c = findMedianSortedArrays(a, 4, b, 4);
    printf("%f", c);
}