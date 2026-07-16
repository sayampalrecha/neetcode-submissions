#include <vector>
#include <unordered_set>

using State = std::unordered_set<int>;
using Candidate = int;

bool isValid(const State& state) {
  return true;
}

std::vector<Candidate> getCandidates(const State& state) {
  return {};
}

viod search(State& state, std::vector<State>& solutions) {
  if (isValidState(state)) {
        // In C++, pushing a state into a vector automatically creates a deep copy
        // of that state. This is the equivalent of `solutions.append(state.copy())`.
        solutions.push_back(state);
        // return; // Uncomment if you want to stop searching deeper once a solution is found
    }

    for (const auto& candidate : getCandidates(state)) {
        state.insert(candidate);    // Python: state.add(candidate)
        search(state, solutions);
        state.erase(candidate);     // Python: state.remove(candidate)
    }
}

std::vector<State> solve(){
  std::vector<State> solutions;
  State state;
  search(state, solutions);
  return solutions;
}
