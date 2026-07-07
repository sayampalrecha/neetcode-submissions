impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut count = [0; 26];

        for (s_byte, t_byte) in s.bytes().zip(t.bytes()) {
            count[(s_byte - b'a') as usize] += 1;
            count[(t_byte - b'a') as usize] -= 1;

        }

        count.iter().all(|&x| x == 0)

    }
}
