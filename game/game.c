#include "game.h"

//菜单函数
int menu()
{
    printf("********************************************\n");
    printf("********************************************\n");
    printf("*************welcome  to saolei*************\n");
    printf("*************   1.      play   *************\n");
    printf("*************   0.      exit   *************\n");
    printf("********************************************\n");
    printf("********************************************\n");
    return 0;
}

//设置雷的位置
void set_mine(char mine[rows][cols])
{
    int count = Count;
    int x = 0;
    int y = 0;
    srand((unsigned)time(NULL));
    while (count)
    {
        x = rand() % 9 + 1;
        y = rand() % 9 + 1;
        if (mine[x][y] == '0')
        {
            mine[x][y] = '1';
            count--;
        }
    }
}

//打印下棋完了显示的界面
void display(char show[rows][cols])
{
    int i = 0;
    int j = 0;
    printf(" ");
    for (i = 1; i < cols - 1; i++)
    {
        printf(" %d ", i);
    }
    printf("\n");
    for (i = 1; i < rows - 1; i++)
    {
        printf("%d", i);
        for (j = 1; j < cols - 1; j++)
        {
            printf(" %c ", show[i][j]);
        }
        printf("\n");
    }
}

//计算雷的个数
int get_num(char mine[rows][cols], int x, int y)
{
    int count = 0;
    if (mine[x - 1][y - 1] == '1') //左上方
    {
        count++;
    }
    if (mine[x - 1][y] == '1') //左边
    {
        count++;
    }
    if (mine[x - 1][y + 1] == '1') //左下方
    {
        count++;
    }
    if (mine[x][y - 1] == '1') //上方
    {
        count++;
    }
    if (mine[x][y + 1] == '1') //下方
    {
        count++;
    }
    if (mine[x + 1][y - 1] == '1') //右上方
    {
        count++;
    }
    if (mine[x + 1][y] == '1') //右方
    {
        count++;
    }
    if (mine[x + 1][y + 1] == '1') //右下方
    {
        count++;
    }
    return count;
}
//扫雷
int Sweep(char mine[rows][cols], char show[rows][cols])
{
    int count = 0;
    int x = 0;
    int y = 0;
    while (count != ((rows - 2) * (cols - 2) - Count))
    {
        printf("请输入坐标：\n");
        scanf("%d%d", &x, &y);
        if (mine[x][y] == '1')
        {
            printf("你踩到雷了！\n");
            return 0;
        }
        else
        {
            int ret = get_num(mine, x, y);
            show[x][y] = ret + '0';
            //set_mine(mine);
            display(show);
            count++;
        }
    }
    printf("恭喜你赢了！\n");
    display(mine);
    return 0;
}

//游戏
int Game(char mine[rows][cols], char show[rows][cols])
{
    set_mine(mine);
    display(show);
    //display(mine);//可以将雷的位置显示出来
    Sweep(mine, show);
    return 0;
}
