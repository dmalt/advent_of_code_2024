package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"sort"
)


func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}


func computeSimilarity(firsts []int, seconds []int) int {
	sum := 0
	for i := 0; i < len(firsts); i++ {
		sum += absInt(firsts[i] - seconds[i])
	}
	return sum
}

func main() {
	// Open a file
	file, err := os.Open("input.txt")
	if err != nil {
		// Handle error if file cannot be opened
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close() // Ensure the file is closed when done

	scanner := bufio.NewScanner(file)

	var firsts []int; var seconds []int

	for scanner.Scan() {
		line := scanner.Text()

		fields := strings.Split(line, "   ")
		first, err1  := strconv.Atoi(fields[0])
		second, err2 := strconv.Atoi(fields[1])
		if (err1 != nil) || (err2 != nil) {
			panic("Shit hit the fan")
		}
		// fmt.Printf("%d -> %d\n", first, second)
		firsts = append(firsts, first)
		seconds = append(seconds, second)
	}
	sort.Ints(firsts); sort.Ints(seconds)


	similarity := computeSimilarity(firsts, seconds)

	// Perform operations with the file
	fmt.Println("The similarity is: ", similarity)
}
