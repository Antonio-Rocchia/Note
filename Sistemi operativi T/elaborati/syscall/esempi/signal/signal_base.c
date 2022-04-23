#include <signal.h>

void gestore(int);
void gestore2(int);

int main(void) {
    /* ... */
    signal(SIGUSR1, gestore);
    signal(SIGUSR2, gestore);
    signal(SIGCHLD,gestore2);

    signal(SIGCHLD,SIG_DFL); /* Reimposto il valore di default */

    /* ... */
}