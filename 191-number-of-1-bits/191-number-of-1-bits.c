int hammingWeight(uint32_t n)
{
    int i = 32;
    int count = 0;
    while (--i >= 0)
    {
        if ((n >> i) & 1)
            count++;
    }
    return count;
}