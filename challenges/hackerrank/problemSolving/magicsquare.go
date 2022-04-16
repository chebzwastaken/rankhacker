package main

import (
	"fmt"
	"math"
)

func formingMagicSquare(s [][]int32) int32 {
	fmt.Println(s)
	var cost float64
	for i := 0; i <= 2; i++ {
		// FIXME add check for when both x1 and x2 are both 5
		// cross check
		if i == 1 {
			fmt.Println(s[i][0], s[i][len(s[i])-1])
			if s[i][0]-10 != s[i][len(s[i])-1] {
				if s[i][0]+s[i][len(s[i])-1]-s[i][0] == s[i][len(s[i])-1] {
					cost += math.Abs(float64(s[i][0] - (10 - s[i][len(s[i])-1])))
					fmt.Println(cost)
				} else {
					cost += math.Abs(float64(s[i][0] - (10 - s[i][len(s[i])-1])))
					fmt.Println(cost)
				}
			}
		}
		// diagnoal check
		if s[0][i]-10 != s[2][(len(s[2])-1)-i] {
			fmt.Println(s[0][i], s[2][(len(s[2])-1)-i])
			if (s[0][i]+s[2][(len(s[2])-1)-i])-s[0][i] == s[2][(len(s[2])-1)-i] {
				cost += math.Abs(float64(s[0][i] - (10 - s[2][(len(s[2])-1)-i])))
				fmt.Println(cost)
			} else {
				cost += math.Abs(float64(s[2][(len(s[2])-1)-i] - (10 - s[0][i])))
				fmt.Println(cost)
			}
		}

		// center check

	}

	if s[1][1] != 5 {
		cost += float64(5 - s[1][1])
	}
	fmt.Println(cost)
	return int32(cost)
}

func main() {
	var s [3][3]int
	var count int = 1
	for i := 0; i <= 2; i++ {
		for j := 0; j <= 2; j++ {
			s[i][j] = count
			count++
		}
	}

	formingMagicSquare([][]int32{{2, 5, 4}, {4, 6, 9}, {4, 5, 2}})
	formingMagicSquare([][]int32{{4, 8, 2}, {4, 5, 7}, {6, 1, 6}})
	formingMagicSquare([][]int32{{4, 9, 2}, {3, 5, 7}, {8, 1, 5}})

}
