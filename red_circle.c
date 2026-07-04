#include <stdio.h>

int main(void)
{
    const int width = 500;
    const int height = 500;
    const int x_circle = 250;
    const int y_circle = 250;
    const int radius = 100;

    FILE *fp = fopen("red_circle.ppm", "w");
    if (fp == NULL) {
        return 1;
    }

    fprintf(fp, "P3\n%d %d\n255\n", width, height);

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            int dx = x - x_circle;
            int dy = y - y_circle;
            if (dx * dx + dy * dy <= radius * radius) {
                fprintf(fp, "255 0 0 ");
            } else {
                fprintf(fp, "255 255 255 ");
            }
        }
        fprintf(fp, "\n");
    }

    fclose(fp);
    return 0;
}