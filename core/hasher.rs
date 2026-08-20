use std::env;
use std::fs::File;
use std::io::{self, Read};
use sha2::{Sha256, Digest};

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: hasher <file_path>");
        std::process::exit(1);
    }
    let mut file = File::open(&args[1])?;
    let mut hasher = Sha256::new();
    let mut buffer = [0; 1024];
    loop {
        let count = file.read(&mut buffer)?;
        if count == 0 { break; }
        hasher.update(&buffer[..count]);
    }
    let result = hasher.finalize();
    println!("{:x}", result);
    Ok(())
}
