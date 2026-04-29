package tests;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.alexander.algorithms.SinglePassAlgorithm;

/***
 * Unit test for Single-Pass algorithm implementation.
 */

class TestSinglePass {
    private final SinglePassAlgorithm SPAlgorithm = new SinglePassAlgorithm();

    @Test
    void testGetMaxValue() {
        // Arrange
        int[] input = {1, 2, 3, 4, 10, 0, 1, 2, 3};
        int maxValue = this.SPAlgorithm.findMaxValue(input);
        IO.print("Max value is: ");
        IO.println(maxValue);

        // Assert
        Assertions.assertEquals(10, maxValue, "The add method should return the sum of its arguments");
    }

    @Test
    void testFindBestProfit() {
        int[] input = {1, 2, 3, 4, 10, 0, 1, 2, 3};
        int bestProfit = SPAlgorithm.findBestProfit(input);
        Assertions.assertEquals(9, bestProfit, "The algorithm returns the best profit from a canonical stock market.");
    }

    @Test
    void testMaxProductSubArray() {
        int[] input = {1, 2, 3, 4, 10, 0, -1, 2, 3};
        int maxProduct = SPAlgorithm.maxProductSubArray(input);
        Assertions.assertEquals(240, maxProduct, "The algorithm returns the maximum product of a subarray.");

        int[] input2 = {1, 2, 3, 4, 10, -1, 2, 3, -4};
        Assertions.assertEquals(5760, SPAlgorithm.maxProductSubArray(input2));
    }
}
