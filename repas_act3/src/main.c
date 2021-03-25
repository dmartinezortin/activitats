/*
 * main.c
 *
 *  Created on: 22 mar. 2021
 *      Author: dani
 */

#include <stdio.h>
#include "functions.h"

void main(){
	int n = requestValue(), arr[n];
	insertValues(&arr, n);
	median(&arr, n);
	getMinValue(&arr, n);
	getMaxValue(&arr, n);
}
