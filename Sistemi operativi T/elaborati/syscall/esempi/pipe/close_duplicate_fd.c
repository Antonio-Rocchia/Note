#include <unistd.h>
#include <stdlib.h>

int main(void) {
    int pipefd[2];

    pipe(pipefd);

    int pid = fork();
    if(pid == 0) {
        close(pipefd[0]); /* Chiudo il lato lettura */

        /* Scrivo nella pipe */

        exit(EXIT_SUCCESS);
    } else if(pid < 0) {
        /* fork error recovery */
        exit(EXIT_FAILURE);
    } /* if pid > 0: Sono il padre*/
        close(pipefd[1]); /* Chiudo il lato scrittura */

        /* Leggo dalla pipe */

        exit(EXIT_SUCCESS);
}