#include <stdio.h>
int main () {

    float jaraktempuh, kelilingtaman, jarijari, phi, kelilinglingkaran;
    kelilingtaman = 5;
    jaraktempuh = 14;
    phi = 3.14;
    kelilinglingkaran = jaraktempuh/kelilingtaman;
    jarijari = (kelilinglingkaran/(phi*2));

    printf ("Diketahui : \n");
    printf ("Pak Dengklek mengelilingi taman = %.f putaran\n", kelilingtaman);
    printf ("Jarak tempuh Pak Dengklek = %.f kilomemeter\n",jaraktempuh);
    printf ("\n");
    printf ("Jawaban : \n");
    printf ("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f kilometer\n", jarijari);
}