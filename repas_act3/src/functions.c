/*
 * functions.c
 *
 *  Created on: 22 mar. 2021
 *      Author: dani
 */

#include <stdio.h>

int requestValue(){
	int n = 0;
	do{
	printf("Quants numeros vols introduir? ");
	scanf("%d", &n);
	}while(n< 1 || n > 50);
	return n;
}

void insertValues(int *arr, int n){
	int i;
	for(i=0;i<n;i++){
		printf("Introdueix un valor: ");
		scanf("%d", arr);
		arr++;
	}
}

void median(int *arr, int n){
	int i, total = 0;
	for(i=0;i<n;i++){
		total += *arr;
		arr++;
	}
	total = total/n;
	printf("La media es: %d\n", total);
}

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
