/*
 * functions.c
 *
 *  Created on: 22 mar. 2021
 *      Author: dani
 */

#include <stdio.h>


//Demana a l'usuari quants valors vol introduir
int requestValue(){
	int n = 0;
	do{
	printf("Quants numeros vols introduir? ");
	scanf("%d", &n);
	}while(n< 1 || n > 50);
	return n;
}

//Introdueix els valors a l'array
void insertValues(int *arr, int n){
	int i;
	for(i=0;i<n;i++){
		printf("Introdueix un valor: ");
		scanf("%d", arr);
		arr++;
	}
}

//Calcula la media de l'array
void median(int *arr, int n){
	int i, total = 0;
	for(i=0;i<n;i++){
		total += *arr;
		arr++;
	}
	total = total/n;
	printf("La media es: %d\n", total);
}

//Obté el valor minim de tots els valors de l'array
void getMinValue(int *arr, int n){
	int i, currentMin = *arr;
	for(i=0;i<n;i++){
		if(currentMin>*arr){
			currentMin = *arr;
		}
		arr++;
	}
	printf("El valor minim es: %d\n", currentMin);
}

//Obté el valor màxim de tots els valors de l'array
void getMaxValue(int *arr, int n){
	int i, currentMax = *arr;
	for(i=0;i<n;i++){
		if(currentMax<*arr){
			currentMax = *arr;
		}
		arr++;
	}
	printf("El valor maxim es: %d\n", currentMax);
}
