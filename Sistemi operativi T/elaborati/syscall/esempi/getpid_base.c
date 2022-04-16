#include <unistd.h>

int main(void) {
    int pid = 0;

    pid = fork();
    if(pid==0) {
        // processo figlio
        printf("La variabile pid = %d\n", pid);
        printf("Il mio pid: %d\n", getpid());
        printf("Il pid del mio processo padre: %d\n", 
                        getppid());
        return 0;
    } else if(pid < 0) {
        perror("Errore durante la fork");
        return -1;
    } else { // if(pid>0)
        // processo padre
        printf("La variabile pid = %d\n", pid);
        printf("Il mio pid: %d\n", getpid());
        printf("Il pid del mio processo padre: %d\n", 
                        getppid());
        return 0;
    }
}