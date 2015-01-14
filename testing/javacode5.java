/* Java code to test the server with
 * Should get response code 5: Exceeds time limit
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 import java.util.*;
 
 class Main{
	
	public static void main(String[] args){
		
		int i=1;
		while(i>0){
			//loop forever
		}
		
		final int ANSWER = 3;
		
		Scanner scanner = new Scanner(System.in);
		String user_num = scanner.nextLine();
		int guess = Integer.parseInt(user_num);
		
		if(guess==ANSWER)
			System.out.println("true");
		else
			System.out.println("false");
	
	}
 }