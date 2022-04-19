#include <stdio.h>
#include <unistd.h>

int main(void)
{
    //  Inizializzo e controllo il valore di ritorno di fork()
    int pid = 0;
    pid = fork();
    if (pid == 0)
    { // Sono il figlio
        // Codice del figlio
        printf("Sono il figlio\n");
        return 0;
    }
    else if (pid > 0)
    { // Sono il padre
        // Codice del padre
        printf("Sono il padre\n");
    }
    return 0;
}