/*
 * PROBLEM STATEMENT FOR ASSIGNMENT 1
 * 
 * Write a Java/C/C++/Python program that contains a string (char pointer) with a value \Hello World’.
 * The program should AND or and XOR each character in this string with 127 and display the result.
 * 
 * Name: Ayush Gala
 * Class: TE 1
 * Roll No: 31128
 */


 /* NOTE: The assignment mentions specefic input of 'Hello World'.
 But for the implementation of this assignment, we will consider all input strings.
 */

import java.util.*;
//import java.io.*;

public class Assignment1 {

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter the input string: ");
        String input = sc.nextLine();
        
        System.out.print("\nThe AND of string with 127 is: ");
        // AND each character with 127
        for(int i=0; i<input.length(); i++)
        {
            System.out.print((char)(input.charAt(i)-'0' & 127));
        }

        System.out.print("\n\nThe XOR of string with 127 is: ");

        // XOR each character with 127
        for(int i=0; i<input.length(); i++)
        {
            System.out.print((char)(input.charAt(i)-'0' ^ 127));
        }

        System.out.println();

        sc.close();


    }

}
