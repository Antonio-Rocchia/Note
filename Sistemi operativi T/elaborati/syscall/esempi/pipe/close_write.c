#include <unistd.h>

int main(void) {
    int pipefd[2];

    pipe(pipefd);

    close(pipefd[1]); /* tutti i file descriptor per il lato scrittura sono chiusi*/
                      /* Scrivo EOF sulla pipe */

    char c;
    read(pipefd[0],&c,1); /* restituisce 0 */
}