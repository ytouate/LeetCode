

int subtractProductAndSum(int n)
{
    int sum = 1;
    int add = 0;
    while (n != 0)
    {
        sum *= n % 10;
        add += n % 10;
        n /= 10;
    }
    return sum - add;
}