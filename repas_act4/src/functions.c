/*
 * functions.c
 *
 *  Created on: 25 mar. 2021
 *      Author: dani
 */

#include <stdio.h>

int validateFormat(long card){
	//Calcula la longitud de la variable card
	int length = 0;
	long aux = card;
	while(aux != 0){
		aux /= 10;
		length += 1;
	}
	return length;
}

int checkType(long card){
	//Comprova el primer numero de la tarjeta
	if(card % 10 == 4 || card % 10 == 5){
		printf("\nEl tipus de tarja es correcte! Continuant amb la compra...\n");
		//En cas de que sigui correcte, retornara 0 i finalitzara el bucle
		return 0;
	} else {
		printf("\nEl tipus de tarja no es correcte... Torna-ho a provar!\n");
		//Cas contrari, retorna 1 i finalitza bucle
		return 1;
	}
}

int requestCard(){
	long card;
	//Demana una tarja i comprova que tingui el format
	do{
		printf("Benvolgut! \nPer continuar amb la compra, introdueix la teva tarja: ");
		scanf("%ld", &card);
	}while(validateFormat(card) != 16 && card > 1);
	return card;
}
