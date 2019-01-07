#if 0
#include <stdio.h>
int main(void)
{
    char **p, i;
    char *strings[] = {
        "one",
        "two",
        "three"};
    p = strings; //strings是地址的地址，所以要定义**p
    for (i = 0; i < 3; i++)
        printf("%s\n", *(p++)); //这里*(p++)是取出存储在数组中的每一个字符串的地址
    return 0;
}
#endif

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#if 0
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int Carry_Val = 0;
    int temp;
    struct ListNode *p1, *p2, *Ret_List;

    Ret_List = l1;

    while (l1 && l2)
    {
        temp = l1->val + l2->val + Carry_Val;
        l1->val = temp % 10;
        Carry_Val = temp / 10;
        p2 = l1;
        l1 = l1->next;
        l2 = l2->next;
    }
    if (!l1)
    {
        p2->next = l2;
        l1 = p2->next;
    }
    while (l1)
    {
        temp = l1->val + Carry_Val;
        l1->val = temp % 10;
        Carry_Val = temp / 10;
        p2 = l1;
        l1 = l1->next;
    }
    if (Carry_Val)
    {
        p1 = (struct ListNode *)malloc(sizeof(struct ListNode));
        p1->next = NULL;
        p1->val = Carry_Val;
        p2->next = p1;
    }

    return Ret_List;
}
#endif

//最优解
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int flag = 0;
    struct ListNode *pSum = NULL;
    struct ListNode *p = NULL;
    struct ListNode *p1 = NULL;

    if (NULL == l1)
    {
        return pSum = l2;
    }
    else if (NULL == l2)
    {
        return pSum = l1;
    }
    else
    {
        pSum = p = malloc(sizeof(struct ListNode));
        memset(p, 0, sizeof(struct ListNode));

        while (l1 || l2 || flag)
        {
            if (p1 != NULL)
            {
                p = malloc(sizeof(struct ListNode));
                memset(p, 0, sizeof(struct ListNode));
                p1->next = p;
            }
            p1 = p;

            if (l1 == NULL && l2 != NULL)
            {
                p->val = l2->val + flag;
                if (p->val >= 10)
                {
                    flag = 1;
                    p->val -= 10;
                }
                else
                {
                    flag = 0;
                }
                l2 = l2->next;
            }
            else if (l2 == NULL && l1 != NULL)
            {
                p->val = l1->val + flag;
                if (p->val >= 10)
                {
                    flag = 1;
                    p->val -= 10;
                }
                else
                {
                    flag = 0;
                }
                l1 = l1->next;
            }
            else if (l1 != NULL && l2 != NULL)
            {
                p->val = l1->val + l2->val + flag;
                if (p->val >= 10)
                {
                    flag = 1;
                    p->val -= 10;
                }
                else
                {
                    flag = 0;
                }
                l1 = l1->next;
                l2 = l2->next;
            }
            else
            {
                p->val = flag;
                flag = 0;
            }
        }

        return pSum;
    }
}
