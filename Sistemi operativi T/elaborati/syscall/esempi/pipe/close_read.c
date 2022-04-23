#include <unistd.h>

int main(void) {
    int pipefd[2];

    pipe(pipefd);

    close(pipefd[0]); /* tutti i file descriptor per la lettura sono chiusi */

    char myString[5] = "Ciao\0";
    write(pipefd[1],myString,5); /* Causa SIGPIPE */
}