/* C code to test the server with
 * Should get response code 5: Exceeds time limit
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <stdio.h>
 int main(){
	const int ANSWER = 3;
	int guess;
	
	int i=1;
	while(i>0){
		//loop forever
	}
	
    //printf( "Guess a number\n" ); //this would be user friendly but is illegal extra output for the contest.
    scanf("%d", &guess);
	
	if(guess==ANSWER)
		printf("true");
	else
		printf("false");
	

    return 0;
 }