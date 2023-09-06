use std::vec::Vec;

fn main() {
	let mut a: i32 = 1;
	let mut b: i32 = 2;
	
	let mut vec1: Vec<i32> = vec![2];

	let mut d = 0;
	
	while d < 4000000{
		let c: i32 = a + b;
		d = c + b;
		if d % 2 == 0{
			vec1.push(d);
		}
		a = b;
		b = c;
	}
	let sum: i32 = vec1.iter().sum();
	println!("Sum is : {}", sum);
}
