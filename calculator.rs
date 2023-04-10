use std::io::stdin;

fn add(vector: Vec<i32>) -> i32{
    let mut total: i32 = 0;
    for i in 0..vector.len(){
        total += vector[i];
    }
    return total;
}

fn sub(vector: Vec<i32>) -> i32{
    let mut total: i32 = vector[0];
    for i in 1..vector.len(){
        total -= vector[i];
    }
    return total;
}

fn mul(vector: Vec<i32>) -> i32{
    let mut total: i32 = vector[0];
    for i in 1..vector.len(){
        total *= vector[i];
    }
    return total;
}

fn div(vector: Vec<i32>) -> i32{
    let mut total: i32 = vector[0];
    for i in 1..vector.len(){
        total /= vector[i];
    }
    return total;
}

fn mods(vector: Vec<i32>) -> i32{
    let mut total: i32 = vector[0];
    for i in 1..vector.len(){
        total %= vector[i];
    }
    return total;
}

fn main(){
    println!("Welcome to basic Calculator (Type help for list of expressions)");
    let mut done = false;
    while !done{
        let mut input_string = String::new();
        stdin().read_line(&mut input_string).expect("Failed to read line...");
        let cmd = &input_string.to_string()[0..4];
        let lst = input_string[4..input_string.len()-1].split(" ");
        let vec: Vec<&str> = lst.collect();
        let mut intvec = vec![0; vec.len()];
        for k in 0..vec.len(){
            match vec[k].trim().parse::<i32>(){
                Ok(i) => intvec[k] = i,
                Err(..) => if vec.len() != 1{ 
                            println!("This was not an integer {}", vec[k]);
                            },
            }
        }
        if cmd == "help"{
            println!("Commands are add, sub, mul, div, mod, exit");
        }
        else if cmd == "add "{
            println!("Your number is: {}", add(intvec));
        }
        else if cmd == "sub "{
            println!("Your number is: {}", sub(intvec));
        }
        else if cmd == "mul "{
            println!("Your number is: {}", mul(intvec));
        }
        else if cmd == "div "{
            println!("Your number is: {}", div(intvec));
        }
        else if cmd == "mod "{
            println!("Your number is: {}", mods(intvec));
        }
        else if cmd == "exit"{
            println!("Goodbye!");
            done = true;
        }
        else{
            println!("Invalid command");
        }
    }
}