use std::vec::Vec;
use std::time::Instant;

fn main() {
	let now = Instant::now();

	let mut a: i128 = 1;
	let mut b: i128 = 2;
	
	let mut vec1: Vec<i128> = vec![2];

	let mut d : i128 = 0;
	
	while d < 4e6 as i128{
		let c: i128 = a + b;
		d = c + b;
		if d % 2 == 0{
			vec1.push(d);
		}
		a = b;
		b = c;
	}
	let sum: i128 = vec1.iter().sum();
	println!("Sum is : {}", sum);
	let elapsed_time = now.elapsed();
	println!("Running fibFunc took {} microseconds.", elapsed_time.as_micros());
}
