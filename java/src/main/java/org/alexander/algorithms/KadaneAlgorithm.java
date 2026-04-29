package org.alexander.algorithms;

/**
 * An implementation of the Kadane’s algorithm.
 * Kadane’s algorithm is an efficient, linear-time (\(O(n)\)) dynamic programming technique used to find the maximum
 * sum of a contiguous subarray within a one-dimensional array of numbers. It operates by iterating through the array
 * once, making a local decision at each element to either extend the previous subarray or start a new one,
 * maintaining \(O(1)\) space complexity.
 */
public class KadaneAlgorithm {

    /**
     * Calculate the maximum sum of subarray in a given array.
     * @param input: array of numbers.
     * @return int: The sum of the continuous sub array.
     */
    public int findMaxSubArraySum(int[] input){
        int maxSoFar = 0;
        int currentMax = 0;
        for(int value: input){
            currentMax = Math.max(value, currentMax+value);
            maxSoFar = Math.max(currentMax, maxSoFar);
        }
        return maxSoFar;
    }

    /***
     * Calculate the minimum sum of subarray of a given array.
     * @param input: array of integer values.
     * @return int: The minimum sum of the subarray.
     */
    public int findMinSubArraySum(int[] input){
        int minSoFar = input[0];
        int currentMin = 0;
        for(int value: input){
            currentMin = Math.min(value, currentMin+value);
            minSoFar = Math.min(currentMin, minSoFar);
        }
        return minSoFar;
    }

    /***
     * Calculate the maximum sum of a circular subarray from a given array.
     * @param input: Array of integer values.
     * @return int: The minimum sum of the subarray.
     */
    public int findMaxCircularSubArraySum(int[] input){
        int totalSum = 0;
        int currentMax = 0;
        int currentMin = 0;
        int maxSoFar = input[0];
        int minSoFar = input[0];

        for(int value: input){
            // Calculate the maximum sum of a subarray.
            currentMax = Math.max(value, currentMax+value);
            maxSoFar = Math.max(maxSoFar, currentMax);

            //Calculate the minimum sum of a subarray.
            currentMin = Math.min(value, currentMin+value);
            minSoFar = Math.min(minSoFar, currentMin);

            // Calculate the total sum of the array
            totalSum += value;
        }

        if(minSoFar == totalSum){
            return maxSoFar;
        }
        return totalSum - minSoFar;
    }
}
