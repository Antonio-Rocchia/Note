#include <sys/stat.h>
#include <stdio.h>

int main(void) {
    printf("Mode 1: %4o\t", S_IRWXU);
    printf("Mode 2: %4o\t", S_IROTH|S_IWOTH);
    printf("Mode 3: %4o\t", S_IRWXU|S_IRWXG|S_IROTH|S_IWOTH);
}