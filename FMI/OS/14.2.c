#include <stdio.h>
#include <stdlib.h>

void main(int argc, char *argv[]) {
	int status;
	for(int i = 1; i < argc; i++) {
		int p_id = fork();
		if(p_id != 0) {
			// printf("%d waiting for %d\n", getpid(), p_id);
			waitpid(p_id, &status, 0);
			printf("%d - %d\n", p_id, status);
		} else {
			// printf("%d executing %s\n", getpid(), argv[i]);
			execlp(argv[i], argv[i], NULL);
			exit(-1);
		}
	}
}
