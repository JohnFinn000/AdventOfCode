use std::fs;

fn calc_fuel(mass: i32) -> i32 {
    let mut fuel = (mass / 3) - 2;
    if fuel > 0 {
        let new_fuel = calc_fuel(fuel);
        if new_fuel > 0 {
            fuel += new_fuel;
        }
    }
    return fuel
}

fn parse_input(filename: &str) {

    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mass_list = contents.trim().split("\n");
    let mut total_fuel = 0;
    for mass in mass_list {
        let mass_int = mass.parse::<i32>().unwrap();
        total_fuel += calc_fuel(mass_int)
    }   
    println!("{}", total_fuel)
}

fn main() {
    parse_input("1_input.txt")
}
