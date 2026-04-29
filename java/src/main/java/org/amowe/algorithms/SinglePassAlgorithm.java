/***
 *  single-pass algorithm (or one-pass algorithm) is a streaming algorithm that processes data in a single sequential
 *  scan, meaning it reads input data only once without going back to previous data points
 * . To handle large datasets or data streams efficiently, these algorithms typically maintain a small, evolving
 * "state" (or buffer) to update results incrementally.
 */
package org.amowe.algorithms;

public class SinglePassAlgorithm {

    /***
     * Find the maximum value in an array of integers.
     * @param input: array of positive integers.
     * @return int: integer of the maximum value in a given array.
     */
    public int findMaxValue(int[] input) {
        int max = 0;
        for (int value : input) {
            if (max < value) max = value;
        }
        return max;
    }

    /***
     * Find the best profit from a canonical stock market.
     * At day i, pretend you sell today -> profit = price[i] - minPriceSoFar
     * @param prices: array of integers representing the stock prices at different time intervals.
     * @return int: Value for the best profit.
     */
    public int findBestProfit(int[] prices){
        int minPriceSoFar = Integer.MAX_VALUE;
        int bestProfit = 0;
        for(int price:  prices){
            minPriceSoFar = Math.min(price, minPriceSoFar);
            bestProfit = Math.max(bestProfit, price - minPriceSoFar);
        }
        return bestProfit;
    }

    /**
     * Returns the maximum product of subarray.
     * @param input: Array of integer values.
     * @return int: the maximum product of subArray.
     */
    public int maxProductSubArray(int[] input){
        int minProduct = 1;
        int maxProduct = 0;
        for (int value: input){
           maxProduct = Math.max(maxProduct, minProduct*value);
           minProduct = minProduct * value;
        }
        return Math.max(minProduct, maxProduct);
    }
}


