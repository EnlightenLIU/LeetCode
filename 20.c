//栈来解决
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
bool isValid(char *s)
{
    //bool t = true;
    //bool f = false;
    int n = strlen(s);
    char *temp = (char *)malloc(sizeof(char) * (n + 1) / 2);
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{')
        {
            temp[k] = s[i];
            k++;
        }
        else
        {
            if (k == 0)
            {
                return false;
            }
            else
            {
                if (s[i] == ')' && temp[k - 1] != '(' || s[i] == ']' && temp[k - 1] != '[' || s[i] == '}' && temp[k - 1] != '{')
                {
                    //printf("%d", f);
                    return false;
                }
            }
            temp[k - 1] = '\0';
            k--;
        }
    }
    return strlen(temp) == 0;
}

void main()
{
    char *string = {"{}(]"};
    //scanf("%s", &string);
    isValid(string);
}
