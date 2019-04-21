package com.frankie;

import org.junit.Test;
import static org.junit.Assert.*;

public class ArraySquareTest {

    @Test
    public void compTrue() {
        int[] a  = {121, 144, 19, 161, 19, 144, 19, 11};
        int[] b  = {121, 14641, 20736, 361, 25921, 361, 20736, 361};
        assertTrue(ArraySquare.comp(a,b));
    }

    @Test
    public void compFalse() {
        int[] a = {1, 2, 3};
        int[] b = {1, 4, 6};
        assertFalse(ArraySquare.comp(a,b));
    }

    @Test
    public void nullArray() {
        int[] a = {4, 5, 6};
        int[] b = null;
        assertFalse(ArraySquare.comp(a,b));
    }

    @Test
    public void diffLenArr() {
        int[] a = {4, 5, 6};
        int[] b = {16, 36};
        assertFalse(ArraySquare.comp(a,b));
    }
}