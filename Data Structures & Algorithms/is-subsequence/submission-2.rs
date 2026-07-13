impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        
        let mut s_iter = s.chars();
        let mut next_char = s_iter.next();

        if next_char.is_none() {
            return true;
        }

        for c in t.chars() {
            if Some(c) == next_char {
                next_char = s_iter.next();

                if next_char.is_none() {
                    return true;
                }
            }
        }
        false
    }
}