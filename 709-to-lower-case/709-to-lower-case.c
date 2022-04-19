
#include "ctype.h"
char * toLowerCase(char * s)
{
    int i;
    i = 0;
    while (s[i])
    {
        if (s[i] >= 'A' && s[i] <= 'Z')
        {
            s[i] = tolower(s[i]);
        }
        i++;
    }
    return(s);
}