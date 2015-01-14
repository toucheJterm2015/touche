/* C++ code to test the server with
 * Should get response code 2: Forbidden word in source
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 #include <iostream>
 #include <fstream>
 using namespace std;
 
  /* the system will currently reject a .c file for Forbidden Words if it contains
  * "system" or "open", even as strings or in a comment. We want to fix that.
  * Therefore, let us try to open a file in this code. It should compile, but our
  * system should reject it. Later iterations of the system should be able to remove 
  * this comment but leave the problematic code and reject it  or remove the
  * problematic code but leave this comment and accept it. */
 
 int main(){
	const int ANSWER = 3;
	int guess;
	
	fstream myfile;
	myfile.open ("illegal.txt");
	myfile << "I'm not allowed to use these keywords to read or write files.";
	myfile.close();
	
	cin >> guess;
	
	if(guess==ANSWER)
		cout << "true";
	else
		cout << "false";
	
	return 0;
 }