use std::vec::Vec;
use std::time::Instant;
use itertools::Itertools;

fn main() {
    let now = Instant::now();

    let mut vec1: Vec<i32> = vec![];

    let mut d: i32 = 0;

    while d < 1000{
        if d % 3 == 0{
            vec1.push(d);
        }
        if d % 5 == 0{
            vec1.push(d);
        }
        d += 1;
    }
    let elapsed_time = now.elapsed();
	println!("Running took {} microseconds.", elapsed_time.as_micros());
    let vec1unique: Vec<i32> = vec1.into_iter().unique().collect();
    let sum: i32 = vec1unique.iter().sum();
    println!("Sum is: {}", sum);
}

