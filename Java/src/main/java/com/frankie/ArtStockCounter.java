package com.frankie;

import java.util.HashMap;
/*
Challenge: give list of arts in String[]{"ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060", ......} format
list of categories to be collected in String[]{"A","B","C", ....} format
In example, "ROXANNE 102".
First letter "R" indicates the art category of this art piece
Number after space is the current count of this specific art piece "ROXANNE"
Group list of arts by art categories and return string showing the count of each art category in (A : countA) - (B : countB) - (C : countC) .... format
if either the list of arts or list of categories is empty, return ""

String[] art = new String[]{"ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"};
String[] letter = new String[]{"B","R","D","X"};
System.out.println(ArtStockCounter.stockSummary(art,letter));
 */
public class ArtStockCounter {

    public static String stockSummary(String[] lstOfArt, String[] lstOf1stLetter) {
        // initiate a Map to count arts by category
        HashMap<String,Integer> artCount = new HashMap<>();

        //if no list of arts or list of categories, return ""
            if ((lstOfArt.length == 0) || (lstOf1stLetter.length == 0)){
                return "";
        }

        // put art category as key into artCount accumulator and 0 as art count
        for (String letter : lstOf1stLetter){
            artCount.put(letter,0);
        }

        // loop through list of art
        for (String item : lstOfArt) {
            String artName = item.split(" ")[0];
            String artCategory = Character.toString(artName.charAt(0));
            Integer artQuantity = Integer.parseInt(item.split(" ")[1]);
            // check if the information of this art category should be collected
            if (artCount.keySet().contains(artCategory)) {
                artCount.put(artCategory, artCount.get(artCategory) + artQuantity);
            }
        }

        // Convert map to desired output format (A : count) - (B : count) ...
        StringBuilder result = new StringBuilder("");
        int keycount = 1;
        for (String key : artCount.keySet()){
            result.append("(").append(key).append(" : ").append(artCount.get(key)).append(")");
            // if there is more items in the keyset, append " - "
            if (keycount != artCount.keySet().toArray().length){
                result.append(" - ");
                keycount++;
            }
        }
        return result.toString();
    }
}
