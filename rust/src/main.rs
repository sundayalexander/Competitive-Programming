mod algorithms;

use std::cmp::max;


fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
    //Calculate the initial window sum
    let window_size = k as usize;
    let mut window_sum: i32 = 0;
    for index in 0..window_size{
        window_sum += nums[index];
    }
    let mut current_sum = window_sum;
    let nums_length = nums.len();
    let max_loop = nums_length - window_size;

    for index in 0..max_loop {
        current_sum = current_sum + (nums[index + window_size] - nums[index]);
        println!("{} - {}", current_sum, nums[index + window_size]);
        window_sum = max(window_sum, current_sum);
    }

    window_sum as f64/k as f64
}

fn main() {
    let nums: Vec<i32> = vec![1,12,-5,-6,50,3];
    let k = 4;
    let result = find_max_average(nums, k);
    println!("{:?}", result);
}
