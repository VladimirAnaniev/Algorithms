#include <stdio.h>
#include <stdlib.h>

/*
	напишете програма на С, която получава като командни параметри две команди без аргументи. Изпълнява ги едновременно и извежда на стандартния изход номера на процеса на първата завършила успешно. Ако нито една не завърши успешно, извежда  -1
*/

void main(int argc, char *argv[]) {
	if(fork()) {
		if(fork()) {
			int status, pid;
			
			for(int i = 0; i <= 1; i++) {
				pid = waitpid(-1, &status, 0);
				if (status == 0) {
					printf("%d\n", pid);
					exit(0);
				}
			}

			printf("No successful calls\n");
			exit(-1);
		} else {
			execlp(argv[2], argv[2], 0);
			exit(-1);
		}
	} else {
		execlp(argv[1], argv[1], 0);
		exit(-1);	
	}
}
