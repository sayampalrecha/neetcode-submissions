impl Solution {
    pub fn num_rescue_boats(mut people: Vec<i32>, limit: i32) -> i32 {

        people.sort();

        let mut l = 0;
        let mut r = people.len() - 1;
        let mut boats = 0;

        while l <= r {
            if people[l] + people[r] <= limit {
                l+=1
            }

            if r == 0 {
                boats += 1;
                break;
            }
            r -= 1;
            boats +=1;
        }
        boats

    }
}
