package com.frankie;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.ArrayList;

public class RectangleToSquaresTest {

    @Test
    public void sqInRect1() {
        ArrayList<Integer> result = RectangleToSquares.sqInRect(3, 5);
        Integer[] arr = {3,2,1,1};
        assertArrayEquals(arr, result.toArray());
    }

    @Test
    public void sqInRect2() {
        ArrayList<Integer> result = RectangleToSquares.sqInRect(3, 2);
        Integer[] arr = {2,1,1};
        assertArrayEquals(arr, result.toArray());
    }

    @Test
    public void sqIntRectNull () {
        ArrayList<Integer> result = RectangleToSquares.sqInRect(6,6);
        assertNull(result);
    }
}