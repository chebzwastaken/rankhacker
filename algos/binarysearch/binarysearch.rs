fn binary_search(arr: [i32; 5], target: i32) -> bool {
    println!("length of array: {}, target is: {}", arr.len(), target);

    let mut low: usize = 0; 
    let mut high: usize = arr.len() - 1;

    while low <= high {
        let mid: usize = (low + high) / 2; 

        if arr[mid] > target {
            high = mid - 1
        }
        else if arr[mid] < target {
            low = mid + 1
        }
        else {
            return true
        }
    }
    return false;
}
fn main() {
    let arr: [i32; 5] = [1, 2, 3, 4, 5]; 
    let target: i32 = 1;
    if binary_search(arr, target) {
        println!("yay we found it");
    }
    else {
        println!(":(");
    } 
}
