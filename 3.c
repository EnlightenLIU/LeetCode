#include <stdio.h>
#include <string.h>
int lengthOfLongestSubstring(char *s)
{

    int maxlen = 0, currlen = 0;
    int table[128], i, j, start = 0;
    memset(table, 0, sizeof(table));
    for (i = 0; s[i] != '\0'; ++i)
    {
        int num = ++table[s[i]];
        if (num == 2)
        {
            if (currlen > maxlen)
            {
                maxlen = currlen;
            }
            for (j = start; j < i; ++j)
            {
                if (s[j] == s[i])
                {
                    table[s[j]] = 1; //保证了num不超过2
                    start = j + 1;
                    break;
                }
                else
                {
                    --currlen;
                    table[s[j]] = 0; //保证了num不超过2
                }
            }
        }
        else
        {
            ++currlen;
        }
    }
    if (currlen > maxlen)
    {
        maxlen = currlen;
    }

    return maxlen;
}

int main()
{

    //    char s[] = "abcdefghiadsdhajdasdsa";
    char s[] = "abcacbabcda";
    //char s[] = "aaaaaaaa";

    int maxlen = lengthOfLongestSubstring(s);

    printf("%d", maxlen);

    return 0;
}

//最优解(不懂)
int max(int i, int j)
{
    if (i > j)
    {
        return i;
    }
    else
    {
        return j;
    }
}
int lengthOfLongestSubstring(char *s)
{
    int count[256] = {[0 ... 255] = -1};
    int len = strlen(s);
    int left = 0, right = 0;
    int res = 0;
    if (len == 0)
    {
        return 0;
    }
    else
    {
        for (right; right < len; right++)
        {
            left = max(count[s[right]], left);
            res = max(res, right - left + 1);
            count[s[right]] = right + 1;
        }
    }
    return res;
}