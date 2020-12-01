use std::env;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::process;
use std::vec::Vec;

fn main() -> io::Result<()> {
  let args: Vec<String> = env::args().collect();
  if args.len() < 2 {
    println!("please pass a filename as arg");
    process::exit(1);
  }
  let filename = &args[1];
  let file = File::open(filename)?;
  let reader = BufReader::new(file);
  let mut xs: Vec<u32> = Vec::new();
  for line in reader.lines() {
    xs.push(line.unwrap().parse::<u32>().unwrap())
  }
  xs.sort();

  let result: String = find_matches(xs);
  println!("{}", result);

  Ok(())
}

fn find_matches(xs: Vec<u32>) -> String {
  for (i, x) in xs.iter().enumerate() {
    for (j, y) in xs[..i].iter().enumerate() {
      for z in &xs[..j] {
        if x + y + z == 2020 {
          return format!("{}, {}, {}, sum: {}", x, y, z, x * y * z);
        }
      }
    }
  }
  return String::from("no matches found");
}
