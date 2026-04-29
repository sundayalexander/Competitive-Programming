package tests;

import org.alexander.algorithms.KadaneAlgorithm;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

/***
 * Unit test for Kadane algorithm implementation.
 */
class TestKadaneAlgorithm {
    private KadaneAlgorithm kda = new KadaneAlgorithm();
    private final int[] input = {2, 3, -8, 7, -1, 2, 3};

    @Test
    void testMaxSubArray(){
        Assertions.assertEquals(11, this.kda.findMaxSubArraySum(this.input));
    }

    @Test
    void testMinSubArray(){
        Assertions.assertEquals(-8, this.kda.findMinSubArraySum(this.input));
    }

    @Test
    void testMaxCircularSubArray(){
        int[] input = {8, -8, 9, -9, 10, -11, 12};
        Assertions.assertEquals(22, this.kda.findMaxCircularSubArraySum(input));
    }
}
