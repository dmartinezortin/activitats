/*
 * main.c
 *
 *  Created on: 25 mar. 2021
 *      Author: dani
 */

#include <stdio.h>
#include "functions.h"

void main(){
	int aux = 1;
	double card;
	while(aux == 1){
		card = requestCard();
		aux = checkType(card);
	}
}
