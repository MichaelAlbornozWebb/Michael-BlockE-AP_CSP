#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//Michael Albornoz
//Recover

typedef uint8_t BYTE; //instilize BYTE constant

int main(int argc, char *argv[])
{
    BYTE buffer[512]; //make 8 byte constant

    if(argc!=2) //kills program when ran incorrectly
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r"); //opens file
    int counter = 0; //counter for naming files
    char filename[8]; //naming file

    if(f==NULL)
    {
        return 2;
    }

    FILE *img; //file

    while(fread(buffer, sizeof(BYTE)*512, 1, f)==1)
    {
        if (buffer[0] == 0xff)
        {
            if (buffer[1] == 0xd8)
            {
                if (buffer[2] == 0xff)
                {
                    if ((buffer[3] & 0xf0) == 0xe0) //all if statement to detect JPG image
                    {
                        sprintf(filename, "%03i.jpg", counter); //prints pixels on img
                        counter = counter + 1; //counter
                        img = fopen(filename, "w"); //opens files from line 38 to write onto
                    }
                }
            }
        }

        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE)*512, 1, img); //prints JPG it on the file
        }

    }
    fclose(img);

    fclose(f); //closes files

    return 0;
}
