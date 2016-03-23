#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
int *unsafe;
const int size = 1000000000;
int main(){
	unsafe = (int*) malloc(sizeof(int));
	*unsafe = 0;
	int i;
	int pid;
//	printf("%p\n",unsafe);
	pid = fork();
	if(!pid){
		for(i=size; i>0; i--){
			(*unsafe)++;
//			printf("tusia = %d address = %p \n", *unsafe, unsafe);
		}	
	free(unsafe);
	}
	else {
		for(i=size; i>0; i--){
			(*unsafe)--;
//			printf("tusia = %d address = %p\n", *unsafe, unsafe);
		}
	free(unsafe);
	}
	return 0;

}












