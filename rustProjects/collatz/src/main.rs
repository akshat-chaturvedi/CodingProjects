use std::time::Instant;

fn collatz(x: i64) -> i64 {
    let mut count: i64 = 1;
    let mut y = x;
    while y != 1 {
        if y % 2 == 0 {
            y /= 2;
        }
        else {
            y = 3*y + 1;
        }
        count += 1;
    }
    return count
}

fn main() {
    let now = Instant::now();

    let mut biggestStartingValue = 0;
    let mut longestChain = 0;
    for i in 1..1000000 {
        let mut current = collatz(i);
        if current > longestChain {
            biggestStartingValue = i;
            longestChain = current;
        }
    }
    println!("The biggest starting value is {}", biggestStartingValue);
    let end_time = Instant::now();
    let elapsed_time = end_time.duration_since(now);
	println!("Running collatz took {:?}.", elapsed_time);
}
