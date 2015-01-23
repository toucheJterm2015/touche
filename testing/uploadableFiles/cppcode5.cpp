/* C++ code to test the server with
 * Should get response code 5: Exceeds time limit
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <iostream>
 using namespace std;
 
 int main(){
	const int ANSWER = 3;
	int guess;
	
	int i=1;
	while(i>0){
		//loop forever
	}
	
	cin >> guess;
	
	if(guess==ANSWER)
		cout << "true";
	else
		cout << "false";
	
	return 0;
 }