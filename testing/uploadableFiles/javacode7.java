/* Java code to test the server with
 * Should get response code 7: Format Error
 * Problem: write code to tell people whether they've guessed the right number (which is 3)
 *  */
 
 import java.util.*;
 
 class Main{
	
	public static void main(String[] args){
		
		final int ANSWER = 3;
		
		Scanner scanner = new Scanner(System.in);
		String user_num = scanner.nextLine();
		int guess = Integer.parseInt(user_num);
		
		if(guess==ANSWER)
			System.out.println("true ");//the extra spaces are just different enough to mess up the automatic grading, even though a human user would not notice
		else
			System.out.println("false ");
	
	}
 }