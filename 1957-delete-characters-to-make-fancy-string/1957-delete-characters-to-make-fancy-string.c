
#include <malloc.h>
char * makeFancyString(char * s)
{
    int i;
    int j;
    char *string = s;
    if (!s)
        return(NULL);
    j = 0;
    i = 0;
    while (s[i])
    {
        while (s[i] == s[i + 1] && s[i + 1] == s[i + 2])
            i++;
        string[j++] = s[i++];
    }
    string[j] = '\0';
    return(string);
}