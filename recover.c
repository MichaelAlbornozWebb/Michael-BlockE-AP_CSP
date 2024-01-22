#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    BYTE buffer[512];

    if(argc!=2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    int counter = 0;
    char filename[8];

    if(f==NULL)
    {
        return 2;
    }

    FILE *img;

    while(fread(buffer, sizeof(BYTE)*512, 1, f)==1)
    {
        if (buffer[0] == 0xff)
        {
            if (buffer[1] == 0xd8)
            {
                if (buffer[2] == 0xff)
                {
                    if ((buffer[3] & 0xf0) == 0xe0)
                    {
                        sprintf(filename, "%03i.jpg", counter);
                        counter = counter + 1;

                        img = fopen(filename, "w");

                        fwrite(buffer, sizeof(BYTE)*512, 1, img);
                    }
                }
            }
        }
    }
    fclose(img);

    fclose(f);

    return 0;
}
