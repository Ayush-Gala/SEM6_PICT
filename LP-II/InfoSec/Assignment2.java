/*
 *  PROBLEM STATEMENT FOR ASSIGNMENT 2
 * 
 *  Write a Java/C/C++/Python program to perform encryption and decryption using the
 *  method of Transposition technique.
 * 
 */


import java.util.*;
// import java.io.*;

public class Assignment2 {
    
    // Encryption function
    public static String encrypt(String input, int key)
    {
        // Create a string to store the encrypted string
        String encrypted = "";
        return encrypted;
    }

    // Decryption function
    public static String decrypt(String input, int key)
    {
        // Create a string to store the decrypted string
        String decrypted = "";
        return decrypted;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter the input string: ");
        String input = sc.nextLine();
        System.out.print("Please enter the key: ");
        int key = sc.nextInt();
        sc.close();

        // Encryption
        String encrypted = encrypt(input, key);
        System.out.println("\nEncrypted string: " + encrypted);

        // Decryption
        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted string: " + decrypted);

    }
}
