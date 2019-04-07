package com.frankie;

import java.util.ArrayList;
/*
Credit to g964, creator of this original Codewars challenge
given rectangle with length lng and width wdth.
Find the combination of squares that fill the rectangle

RectangleToSquares.sqInRect(5,3);
 */


public class RectangleToSquares {

    public static ArrayList<Integer> sqInRect(int lng, int wdth) {
        ArrayList<Integer> resultList = new ArrayList<Integer>();
        if (lng == wdth){
            return null;
        }
        while (true) {
            if (lng > wdth) {
                resultList.add(wdth);
                lng -= wdth;
            } else if (lng < wdth) {
                resultList.add(lng);
                wdth -= lng;
            } else {
                resultList.add(lng);
                break;
            }
        }
        return resultList;
    }
}