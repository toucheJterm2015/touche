/* C code to test the server with
 * Should get response code 8: Runtime Error
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <stdio.h>
 int main(){
	const int ANSWER = 3;
	int guess;
	
	int arrayToBreak[2]; //I can manufacture a runtime error by trying to access index 2 or higher in this array.
	int i=2;
	while (i < 4 ){
		printf( arrayToBreak[i]+"\n" );//C is too helpful and won't actually give me a runtime error unless I try to do something with the value I can't access.
		i++;
	}
	
    //printf( "Guess a number\n" ); //this would be user friendly but is illegal extra output for the contest.
    scanf("%d", &guess);
	
	if(guess==ANSWER)
		printf("true");
	else
		printf("false");
	

    return 0;
 }