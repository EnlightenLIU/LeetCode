char *longestCommonPrefix(char **strs, int strsSize)
{
    assert(strs);
    if (strsSize == 0)
    {
        return "";
    }
    if (strsSize == 1)
    {
        return *(strs + 0);
    }
    char *head = *(strs + 0);
    char *end = *(strs + 0);
    char *traval = *(strs + 1);
    char *cur = *(strs + 0);
    // char *traval = *(strs + 1);
    char *ret = NULL;
    //前两个元素的公共前缀
    while (*traval == *end)
    {
        end++, traval++;
    }

    for (int i = 2; i < strsSize; i++)
    {
        cur = *(strs + i);
        traval = *(strs + 0);
        while (*cur == *traval)
        {
            cur++, traval++;
        }
        if (traval < end)
        {
            end = traval;
        }
        if (head == end)//刚才少写了一个等号
        {
            return "";
        }
    }
    ret = (char *)malloc(sizeof(char) * (end - head) + 1);
    for (int i = 0; i < end - head; i++)
    {
        *(ret + i) = *(head + i);
    }
    *(ret + (end - head)) = '\0';
    return ret;
}