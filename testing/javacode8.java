/* Java code to test the server with
 * Should get response code 8: Runtime Error
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 import java.util.*;
 
 class prob1{
	
	public static void main(String[] args){
		
		if(true)
			throw new RuntimeException("Now break.");
		
		final int ANSWER = 3;
		
		Scanner scanner = new Scanner(System.in);
		String user_num = scanner.nextLine();
		int guess = Integer.parseInt(user_num);
		
		if(guess==ANSWER)
			System.out.println(""+true);//the extra spaces will not change a reader's interpretation of feedback, but it's different enough for the computer
		else
			System.out.println(""+false);
	
	}
 }