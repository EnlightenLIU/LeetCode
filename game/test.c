
#include "game.h"

int main()
{
    int input = 0;
    char mine[rows][cols];
    char show[rows][cols];
    int i = 0;
    int j = 0;
    for (i = 0; i < rows - 1; i++)
    {
        for (j = 0; j < cols - 1; j++)
        {
            mine[i][j] = '0';
            show[i][j] = '*';
        }
    }
    menu();
    while (1)
    {
        printf("请选择:");
        scanf("%d", &input);
        if (input == 1)
        {
            printf("进入游戏\n");
            Game(mine, show);
            break;
        }
        else if (input == 0)
        {
            printf("退出游戏！\n");
            exit(0);
            break;
        }
        else
        {
            printf("输入有误！\n");
        }
    }
    return 0;
}
