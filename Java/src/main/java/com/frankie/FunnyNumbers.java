package com.frankie;
/*
Credit to Codewars user g964
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Write a function (n, p) to find if there is an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
if not, return -1
 */


public class FunnyNumbers {
    public static long funnyNumbers(int n, int p) {
        String numberString = Integer.toString(n);
        String[] numberStringList = numberString.split("");
        Integer accumulator = null;

        for (String item : numberStringList){
            if (accumulator == null){
                accumulator = (int)Math.pow(Integer.parseInt(item),p);
                p++;
            } else {
                accumulator += (int)Math.pow(Integer.parseInt(item),p);
                p++;
            }
        }

        if (accumulator % n == 0){
            return accumulator / n;
        } else {
            return -1;
        }
    }
}
