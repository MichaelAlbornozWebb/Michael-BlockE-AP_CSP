#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;

            float avergray = round((red + blue + green) / 3.0);

            image[i][j].rgbtRed = avergray;
            image[i][j].rgbtBlue = avergray;
            image[i][j].rgbtGreen = avergray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;


            float sred = 0.393*(red) + 0.769*(green) + 0.189*(blue);
            float sgreen = 0.349*(red) + 0.686*(green) + 0.168*(blue);
            float sblue = 0.272*(red) + 0.534*(green) + 0.131*(blue);

            if (sred > 255)
            {
                sred = 255;
            }
            if (sblue > 255)
            {
                sblue = 255;
            }
            if (sgreen > 255)
            {
                sgreen = 255;
            }

            image[i][j].rgbtRed = round(sred);
            image[i][j].rgbtBlue = round(sblue);
            image[i][j].rgbtGreen = round(sgreen);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
for (int i = 0; i < height; i++)
    {
    for (int j = 0; j < width / 2; j++)
            {
                RGBTRIPLE temp[height][width];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j];
            }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
                {
                float gridred = 0;
                float gridblue = 0;
                float gridgreen = 0;
                int gridnum = 0;

                for (int o = -1; o <= 1; o++)
                {
                    for (int p = -1; p <= 1; p++)
                    {
                        if (i + o < 0 || i + o > height - 1)
                        {
                            continue;
                        }

                        if (j + p < 0 || j + p > width - 1)
                        {
                            continue;
                        }

                        gridred += image[i + o][j + p].rgbtRed;
                        gridblue += image[i + o][j + p].rgbtBlue;
                        gridgreen += image[i + o][j + p].rgbtGreen;
                        gridnum++;
                    }
                }

                temp[i][j].rgbtRed = round(gridred / gridnum);
                temp[i][j].rgbtBlue = round(gridblue / gridnum);
                temp[i][j].rgbtGreen = round(gridgreen / gridnum);
            }
        }

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                image[i][j].rgbtRed = temp[i][j].rgbtRed;
                image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
                image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            }

        }
    return;
}
