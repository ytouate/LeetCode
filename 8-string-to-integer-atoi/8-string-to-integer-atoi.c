#include <limits.h>

int myAtoi(char * s)
{
    int i = 0;
    int sign;
    unsigned long result;
    sign = 1;
    result = 0;
    while (s[i] == ' ')
        i++;
    if (s[i] == '-' || s[i] == '+')
    {
        if (s[i++] == '-')
            sign = -1;
        else
            sign = 1;
    }
    while (s[i] >= '0' && s[i] <= '9')
    {
        result = result * 10 + s[i] - '0';
        if (result > INT_MAX)
		{
			if (sign == -1)
				return (INT_MIN);
			return (INT_MAX);
		}
        i++;
    }
    return (result * sign);

}