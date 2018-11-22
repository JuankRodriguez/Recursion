#include <iostream>
using namespace std;
 
void hanoi(int num,char A,char C,char B)
{
    if(num==1)
    {
            cout<<"Mueva el bloque "<< num <<" desde "<< A <<" hasta  "<< C << endl;
             
    }
    else
    {
        hanoi(num-1,A,B,C);
        cout<<"Mueva el bloque "<<num<<" desde "<< A <<" hasta  "<<C<<endl;
        hanoi(num-1,B,C,A);
    }
}
 
int main()
{
        int n;
        char A,B,C;
 
        cout<<"Los clavijas son A B C\n";
        cout<<"Numero de discos: ";
        cin>>n;
        hanoi(n,'A','C','B');
   return 0;      
}
/*Lo que realiza el anterior codigo es resolver a lo que son las trorres de hanoi donde en tres pilas; una con un numero n discos
de tamaño creciente, se determina el minimo optimo de pasos que lleva mover todos los discos desde su posicion inicial a otra pila sin colocar 
un disco de mayor tamaño sobre uno de menor tamaño.*/
