// package main


func minCostClimbingStairs(cost []int) int {
    
    downOne := 0
    downTwo := 0

    for i := 2; i<= len(cost); i++ {
        current := min(downOne+cost[i-1],downTwo+cost[i-2])

        downTwo = downOne
        downOne = current
    }
    return downOne
}
