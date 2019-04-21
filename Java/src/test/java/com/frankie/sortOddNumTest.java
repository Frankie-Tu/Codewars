package com.frankie;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Arrays;

public class sortOddNumTest {

    @Test
    public void sortArray() {
        // memory address will likely be different, convert to string for comparison
        assertEquals(Arrays.toString(new int[]{3, 5, 2, 6, 7, 2}), Arrays.toString(sortOddNum.sortArray(new int[]{5, 3, 2, 6, 7, 2})));
    }
}