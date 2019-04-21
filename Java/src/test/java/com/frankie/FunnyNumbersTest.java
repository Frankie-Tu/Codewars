package com.frankie;

import org.junit.Test;
import static org.junit.Assert.*;

public class FunnyNumbersTest {

    @Test
    public void funnyNumbersTest1() {
        assertEquals(1, FunnyNumbers.funnyNumbers(89, 1));
    }

    @Test
    public void funnyNumbersTest2() {
        assertEquals(2,FunnyNumbers.funnyNumbers(695, 2));
    }

    @Test
    public void funnyNumbersTest3() {
        assertEquals(51, FunnyNumbers.funnyNumbers(46288,3));
    }

    @Test
    public void funnyNumbersTest4() {
        assertEquals(-1, FunnyNumbers.funnyNumbers(234,1));
    }
}