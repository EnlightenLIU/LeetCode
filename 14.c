#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
char *longestCommonPrefix(char **strs, int strsSize)
{
    assert(strs);
    if (strsSize == 1)
    {
        //字符串只有一个，直接返回字符串就完事了
        return *(strs + 0);
    }
    if (strsSize == 0)
    {
        //没有字符串，忍不住吐槽一下，这个测试太坑了，还能传0个字符串。
        return "";
    }
    char *head = *(strs + 0);
    char *end = *(strs + 0);    //第一个字符串与后面字符串相同部分尾部
    char *traval = *(strs + 1); //用于在head和end之间走
    char *cur = *(strs + 0);    //cur为当前字符串遍历用指针
    char *ret = NULL;
    while (*end == *traval)
    {
        //得到相同前缀的范围
        end++, traval++;
    }
    for (int i = 2; i < strsSize; i++)
    {
        cur = *(strs + i);
        traval = *(strs + 0);
        while (*traval == *cur)
        {
            traval++, cur++;
        }
        if (traval < end)
        {
            //当traval与end不一致时，说明相同前缀比end - head短，需要调整end指针
            end = traval;
        }
        if (end == head)
        {
            //当end指向头，说明无相同前缀
            return "";
        }
    }
    ret = (char *)malloc(sizeof(char) * (end - head) + 1); //申请空间返回
    for (int i = 0; i < end - head; i++)
    {
        //拷贝字符串
        *(ret + i) = *(head + i);
    }
    *(ret + (end - head)) = '\0'; //别忘了末尾加'\0'
    return ret;
}

void main()
{
    char *s;
    int m;
    printf("enter the strsSize:");
    scanf("%d", &m);
    char *string[m];
    // *string = (char *)malloc(sizeof(char) * m);
    for (int i = 0; i < m; i++)
    {
        printf("enter the %d string:", i + 1);
        //char *j = *(string + i);
        scanf("%s", (string + i)); //输入取地址的处理问题会造成后面出错&
    }
    s = longestCommonPrefix(string, m); //执行到这里就会出错
    printf("%s", s);
#if 0
    char *s;
    char *string[3] = {"flower", "flow", "flight"};
    s = longestCommonPrefix(string, 3);
    printf("%s", s);
#endif
}
