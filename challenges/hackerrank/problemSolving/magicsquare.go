package main

import (
	"fmt"
	"math"
)

func getCost(arr [][]int32, magic_square [3][3]int32) int32 {
	var cost int32 = 0
	for i := 0; i <= 2; i++ {
		for j := 0; j <= 2; j++ {
			cost += int32(math.Abs(float64(arr[i][j] - magic_square[i][j])))
		}
	}
	return cost
}

func formingMagicSquare(s [][]int32) int32 {
	var magic = [8][3][3]int32{
		{{8, 1, 6}, {3, 5, 7}, {4, 9, 2}},
		{{6, 1, 8}, {7, 5, 3}, {2, 9, 4}},
		{{4, 9, 2}, {3, 5, 7}, {8, 1, 6}},
		{{2, 9, 4}, {7, 5, 3}, {6, 1, 8}},
		{{8, 3, 4}, {1, 5, 9}, {6, 7, 2}},
		{{4, 3, 8}, {9, 5, 1}, {2, 7, 6}},
		{{6, 7, 2}, {1, 5, 9}, {8, 3, 4}},
		{{2, 7, 6}, {9, 5, 1}, {4, 3, 8}},
	}

	var min_cost = math.Inf(1)

	for _, magic_square := range magic {
		cost := getCost(s, magic_square)
		min_cost = math.Min(float64(min_cost), float64(cost))
	}
	return int32(min_cost)
}
func main() {
	fmt.Println(formingMagicSquare([][]int32{{2, 5, 4}, {4, 6, 9}, {4, 5, 2}}))
}
