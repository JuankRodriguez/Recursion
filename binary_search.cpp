#include <iostream>
using namespace std;

int main()
{
	int lista[] = {1,2,3,4,5,6,7,8,9,10,11,12}; //lista en la que se hace la lista
	int tam = 11;
	int buscar,trozo;
	buscar = 2;//numero a buscar
	trozo = tam/2;
	int temp = trozo,contador = 0,elemento = lista[trozo];

	
	if(buscar == lista[0] or buscar == lista[tam]){
		cout << "El Elemento existe" << endl;
	}
	else if(buscar < lista[0] or buscar > lista[tam]){
		cout << "El elemento no existe" << endl;
	}
	else
	{
		while( contador <= tam)
		{
			if(buscar > lista[trozo-1] and buscar < lista[trozo+1] ){
				contador = tam;
			}
			else if(buscar < elemento)
			{
				trozo -= temp/2;
				elemento = lista[trozo];
			}
			else if(buscar > elemento){
				trozo += temp /2 - 1;
				elemento = lista[trozo];
				temp = trozo;
			}
			else{
				contador = tam; 
			}
			contador++;
		}
		
		if(buscar == elemento){
			cout << "Existe" << endl;
		}
		else{
			cout << "No existe" << endl;
		}
	}
	
return 0;
}
/*lo que realiza el anterior codigo es una busqueda de un numero en una lista pero de forma binaria, lo que quiere decir que de la lista que tenga va a elegir la mitad y buscara el numero 
en esa mitad ya que si no lo encuentra quiere decir que es posible este en la otra mitad. luego que determina en que mitad esta o no hace lo mismo con la mitad elegida*/

