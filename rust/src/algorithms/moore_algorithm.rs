/**
Story
A large distributed backend system records an error code every time a request fails. Over a long
monitoring window, engineers believe that one particular error code is responsible for the majority
of failures.
- The log stream is extremely large
- You can process entries only once
- Storing frequency counts for all error codes is not feasible
Example
errors = [500, 404, 500, 500, 403, 500, 500]

This function is implemented using Moore majority voting algorithm to find the dominant error type.
*/
fn find_dominant_error_type(nums: &[i32]) -> i32 {
    let mut count:i32 = 0;
    let mut candidate = nums[0];
    let num_len = nums.len();
    for index in 0..num_len {
        if candidate == nums[index] {
            count += 1;
        }else {
            count -= 1;
        }

        if count == 0{
            candidate = nums[index];
            count = 1;
        }
        println!("{} - {}", candidate, count);
    }
    count = 0;
    for index in 0..num_len {
        if candidate == nums[index] {
            count += 1;
        }
    }

    if count > num_len as i32 /2 {
        return candidate;
    }
    return -1;
}


#[test]
fn test_dominant_error_type() {
    let input = [500, 404, 500, 500, 403, 500, 500];
    assert_eq!(find_dominant_error_type(&input), 500);
}