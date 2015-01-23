/* C++ code to test the server with
 * Should get response code 8: Runtime Error
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <iostream>
 #include <stdexcept>
 using namespace std;
 
 int main(){
	const int ANSWER = 3;
	int guess;
	
	int i = 1;
	if(i>0)
		throw runtime_error("Now break.");
	
	cin >> guess;
	
	if(guess==ANSWER)
		cout << "true";
	else
		cout << "false";
	
	return 0;
 }