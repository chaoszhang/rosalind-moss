/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

/**
 *
 * @author Kellie
 */
public class JavaApplication1 {

    /**
     * @param text
     * @param pattern
     * @param args the command line arguments
     */
    public static int patternCount(String text,String pattern){
        int count = 0;
        int counter = 0;
        
        for(int i = 0; i < (text.length() - pattern.length() + 1); i++) {
            if(text.substring(i, (i + pattern.length())).equals(pattern)) {
                counter++;
            }
        }
        
        return counter;
    }
    public static void main(String[] args) {
        // TODO code application logic here
        int result = patternCount("CTCCTTCGCTCCTTCAAGTTACAGCTCCTTCGCTCCTTCACTCCTTCGGCTCCTTCCTCCTTCCTCCTTCTCTCCTTCGCTCCTTCGCTCCTTCGGTCTCCTTCTCTCTCCTCCTTCTGTGGAGGCCGATTCACTCCTTCCCCCCTCCTTCATGCTCCTTCCTCCTTCTCTCCTTCATCTCCTTCGCACTCCTTCCTGATCGCCTCCTTCTACAAACTCCTTCGCTCCTTCTTGTCTCCTTCCTCCTTCCTCCTTCCGCTCCTTCCTCCTTCCTCCTTCTCGTCTCCTTCCTCCTTCTCTCCTTCGAGCTCCTTCACCTCCTTCAGCCTCCTTCTCTCTCCTTCCGCTCCTTCCCTCCTTCACTCCTTCCTCCTTCTAAGCCTCCTTCGAGCTCCTTCCCTCCTTCACCGGTGTTACCTCCTTCCTCCTTCCCTCCTTCTATCTCCTTCTCCTCCTTCAGCAACTCCTTCACTCCTTCCTCCTTCCTCCTTCTCCGGTACTCCTTCCTCCTTCAACTCCTTCCTCCTTCGTGCTCTCCTTCTGTCTCTCCTTCTAAGTCTCCTTCCCTCCTTCTTAGCTCCTTCGTAACTCCTTCCTCCTTCCACTCCTTCTTTCAACACACTCCTTCCCCTCCTTCTCCTCCTTCGCTCCTTCAATCTCTCCTTCCACTCCTTCTCTCCTTCTACGCTCCTTCCTCCTTCCCTCCTTCGAGCATTATGCTCTCCTTCTCCTGCCTCCTTCCTCCTTCCCTCCTTCAAGCATCTCCTCCTCCTTCACCTCCTTCCTCCTTCTAACTCCTTCAGGGATGTCTCCTTCCTCCTTCAACCTCCTTCATTCTCCTTCGGCTCCTTCATCTCCTTCGTAGGATAAGTCTCTCCTTCACGATCATAGCATCTCCTTCCGACTCCTTCATTACTCCTTCCCCTGACACTTCCTCCTTCCTCCTTCCTCCTTCGTCAGATGGCTCCTTCCTCCTTCAAGCTCCTTCACCTCCTTCCACTCCTTC", "CTCCTTCCT");
        int result2 = patternCount("AAGACCAGGTAAAGACCAAGACAAGACCATTCAAGACCAAAGACCAAGAAGACCACAAGACCATCATTAAGACCATAAGACCAGAGGAAGACCACCACAAGACCAAAGACCACAAGACCAAAGACCAAAGACCAGTCAAGACCAAAGACCAAAGACCATTCAAGACCACCACTATCATAAGTTGGCCAAGACCAAAGACCAGAAAGACCATCAAAGACCAGACAAGACCAAGTACACTGGACATATCCAAGACCACGCTAAAGACCAAAGACCATTCAAGACCAAAGACCATAAAGACCACTTTGGAGCGGAAGACCAAAGACCAACAAGACCATCCAAGACCAAAGACCATAAAGACCACAAAGACCAAAGACCAGAAGACCAAAGACCAGTAAGACCACACCCGATCGGACTAAGACCAGGGATGCGAAGACCAGCGAGACACGAATAAGACCAAAGACCATAAGACCAAAGACCATCAAGACCAATTAAGACCAGCAAAGACCAACGGAAGACCAAAAGACCAGGGAAGACCAAAGACCAGAAAGACCAAATCTAAGACCAAAGACCAAAGACCAAAGACCAATTCTAAAGACCACGAAAAGACCACCTTCAAGACCACATAAAGACCACAGTGTTCCTCTAAGACCACCAAAGACCAAAGACCACAAGACCAGAAGACCAAAGACCATTACGTCTAAGACCAGAAGACCAATCTAAAGACCAGCTCGAAGACCACAAGACCACAAGACCATAATCACCTCTAAGACCAAAGACCACAAGACCAACCACAAGACCATAAAGACCACAAGACCATTGTTGATAAGACCAGCATGTGGAAAAGACCAGCAAAGACCATACAAGACCAGAAGACCACATAAGACCAGAACATCAAGACCAATCGAAGACCAGTTGTCGCTAAAGACCAGAAGACCAAAGACCAAAAGACCAAAAGACCAAAGACCAAAGACCA" , "AAGACCAAA");
        System.out.println(result2);

    }
    
}