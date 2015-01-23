/* C++ code to test the server with
 * Should get response code 6: Incorrect Output
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <iostream>
 using namespace std;
 
 int main(){
	const int ANSWER = 3;
	int guess;
	
	cin >> guess;
	
	if(guess!=ANSWER)//wrong equality; gives you the opposite of what you want.
		cout << "true";
	else
		cout << "false";
	
	return 0;
 }