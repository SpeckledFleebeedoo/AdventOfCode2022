use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename).expect("File read successfully");

    let elfs: Vec<&str> = contents.split("\n\n").collect();
    let mut totals: Vec<u32> = Vec::new();

    for elf in elfs {
        let values: Vec<&str> = elf.split("\n").collect();
        let mut total = 0;
        for value in values {
            total += value.parse::<u32>().unwrap();
        }
        totals.push(total);
    }
    totals.sort_by(|a, b| b.cmp(a));
    let top3 = &totals[..3];
    let mut sum: u32 = 0;
    for i in top3 {
        sum += i;
    }
    println!("{:?}", sum)
}
