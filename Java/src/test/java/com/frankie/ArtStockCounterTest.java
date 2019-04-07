package com.frankie;

import org.junit.Test;

import static org.junit.Assert.*;

public class ArtStockCounterTest {

    @Test
    public void stockSummaryTest1() {
        String [] art = new String[] {"ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"};
        String [] letter = new String[]{"B","R","D","X"};
        String result = ArtStockCounter.stockSummary(art,letter);
        String answer = "(B : 364) - (R : 225) - (D : 60) - (X : 0)";
        assertEquals(result, answer);
    }

    @Test
    public void stockSummaryTest2() {
        String [] art = new String[] {"ASDISK 200", "BLOLKI 10", "BIKIKI 20", "DLSIDKS 200", "ASCCIDS 20", "CRTYMKH 001"};
        String [] letter = new String[]{"A","B","C"};
        String result = ArtStockCounter.stockSummary(art,letter);
        String answer = "(A : 220) - (B : 30) - (C : 1)";
        assertEquals(result, answer);
    }

}