/* C++ code to test the server with
 * Should get response code 4: Compile Error (lack of semicolons)
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <iostream>
 using namespace std
 
 int main(){
	const int ANSWER = 3
	int guess
	
	cin >> guess
	
	if(guess==ANSWER)
		cout << "true"
	else
		cout << "false"
	
	return 0
 }