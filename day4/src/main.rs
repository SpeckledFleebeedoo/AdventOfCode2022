use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename).expect("File read successfully");

    let mut total = 0;

    let pairs: Vec<&str> = contents.split("\n").collect();
    for pair in pairs {
        let p: Vec<&str> = pair.split(",").collect();
        let overlap1 = check_overlap(p[0], p[1]);
        // let overlap2 = check_overlap(p[1], p[0]);
        if overlap1 == true {
            total += 1;
        }
    }
    println!("{:?}", total)
}

fn check_overlap(r1: &str, r2: &str) -> bool {
    let (start1, finish1) = pair_to_values(r1);
    let (start2, finish2) = pair_to_values(r2);
//  if start1 <= start2 && finish1 >= finish2 {
    if finish1 < start2 || start1 > finish2 {
        return false
    } else {
        return true
    }
}

fn pair_to_values(range: &str) -> (u32, u32) {
    let x: Vec<&str> = range.split("-").collect();
    let start = x[0].parse().unwrap();
    let finish = x[1].parse().unwrap();

    return (start, finish)
}


