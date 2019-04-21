package com.frankie;

import java.util.Collections;
import java.util.ArrayList;

/*
Credit to Codewars user fyvfyv
Given input array, sort odd numbers in ascending order and keep even numbers in their places
return the sorted array
example:
    inputArray = [5, 3, 2, 6, 7, 2]
    return [3, 5, 2, 6, 7, 2]
 */

public class sortOddNum {
    public static int[] sortArray(int[] array) {
        // create result array with the same length as input arr
        int [] resultArr = new int[array.length];
        int currentIndex = 0;
        ArrayList<Integer> oddList = new ArrayList<>();
        // Arraylist holding index of odd numbers in input array
        ArrayList<Integer> oddIndex = new ArrayList<>();

        // Append even numbers into result array as they are not sorted
        for (int item : array){
            if (item % 2 == 0){
                resultArr[currentIndex] = item;
            } else {
                oddList.add(item);
                oddIndex.add(currentIndex);
            }
            currentIndex++;
        }
        Collections.sort(oddList);

        for (int i = 0; i < oddList.size(); i++){
            resultArr[oddIndex.get(i)] = oddList.get(i);
        }
        return resultArr;
    }
}
