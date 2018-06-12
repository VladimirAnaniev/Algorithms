#include <stdio.h>
#include <stdlib.h>

void main(int argc, char* argv[]) {
	int proc_id = fork();
	if(proc_id != 0){
		int status, r;
		wait(&status);
		if(status == 0) {	
			printf("%s\n", argv[1]);
		}
	} else {
		execlp(argv[1], "");
		exit(-1);
	}
}
