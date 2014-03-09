package main

import (
    "fmt"
    "os"
)

func main() {
    input := os.Args[1]
    permute(input, 0)
}

func permute(input string, start int) {
    s := len(input)
    if start >= s {
        fmt.Printf("%s\n", input)
    } else {
        permute(input, start + 1)
    }
    for i := start + 1; i < s; i++ {
        output := []byte(input)
        output[start], output[i] = output[i], output[start]
        newinput := string(output)
        permute(newinput, start + 1)
    }
}
