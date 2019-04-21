package com.frankie;

import java.util.ArrayList;
/*
Credit to Codewars user g964
given array a and b, find if they are the "same"
A = [121, 144, 19, 161, 19, 144, 19, 11]
B = [121, 14641, 20736, 361, 25921, 361, 20736, 361]  = [ 11^2 , 121^2, 144^2, 19^2, 161^2, 19^, 144^2, 19^2]
condition: same in the sense that array B contains ONLY the values from array A squared regardless of order.
*/
public class ArraySquare {
    public static boolean comp(int[] a, int[] b) {
        ArrayList<Integer> arrA = new ArrayList<>();
        ArrayList<Integer> arrB = new ArrayList<>();

        if (a == null || b == null || a.length != b.length) {
            return false;
        } else if ( a.length == 0){
            return true;
        }

        for (int num : a){
            arrA.add((int)Math.pow(num,2));
        }

        for (int num : b){
            arrB.add((int)num);
        }

        for (int num : arrB){
            // check if the squared number can be found, if yes pop the number else return false
            if (arrA.indexOf(num) == -1){
                return false;
            } else {
                arrA.remove(arrA.indexOf(num));
            }
        }
        // managed to make it to the end of the code, condition must be true
        return true;
    }
}
