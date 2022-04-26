#include <fcntl.h>

int main()
{
    int fd1,fd2,fd3;

    fd1=open("path/to/file/", O_RDONLY);
    if(fd1<0) {
        perror("open fallita");
    }
    /* ... */
    fd2=open("path/to/file2/", O_WRONLY);
    if(fd2<0) {
        perror("open in scrittura fallita");

        fd2=open("path/to/file2/", O_WRONLY|O_CREAT, 0777);
    }
    /* Omogeneo: apertura di un dispositivo */
    fd3=open("/dev/dispositivo", O_WRONLY);
    /* ... */
}