#include<stdio.h>
#include<stdlib.h>

void display(float matrix[13][10]){
	for (int i=0; i<13; i++){
		for(int j=0; j<10; j++)
			printf("%d\t", matrix[i][j]);
		printf("\n");
	}
}

int main(){
float c[13][10];
display(c);
}
