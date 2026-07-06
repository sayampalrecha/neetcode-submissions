impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 2 {
            return n;
        }
        let mut one_step_behind = 2;
        let mut two_steps_behind = 1;
        let mut current_ways = 0;

        for _ in 3..=n {
            current_ways = one_step_behind + two_steps_behind;
            two_steps_behind = one_step_behind;
            one_step_behind = current_ways;
        }
        current_ways

    }
}
