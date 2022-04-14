package main

func catAndMouse(x int32, y int32, z int32) string {
	var distanceA int32
	var distanceB int32

	distanceA = z - x
	distanceB = z - y

	if distanceA < 0 {
		distanceA = distanceA * -1
	} else if distanceB < 0 {
		distanceB = distanceB * -1
	}

	if distanceA < distanceB {
		return "Cat A"
	} else if distanceA > distanceB {
		return "Cat B"
	} else {
		return "Mouse C"
	}

}

func main() {
	catAndMouse(1, 2, 3)
}
