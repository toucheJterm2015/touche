/* C code to test the server with
 * Should get response code 7: Format Error
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <stdio.h>
 int main(){
	const int ANSWER = 3;
	int guess;
	
    //printf( "Guess a number\n" ); //this would be user friendly but is illegal extra output for the contest.
    scanf("%d", &guess);
	
	if(guess==ANSWER)
		printf("true ");//the extra space is just enough to throw off the judging software. It's not the same answer as "true".
	else
		printf("false ");
	

    return 0;
 }