package main

import (
	"fmt"
	"sync"
)

func Concurren() {
	ch := make(chan int, 11)

	go func() {
		for i := 1; i < 20; i++ {
			ch <- i
			fmt.Println("Sending:", i)
		}
	}()

	for i := 1; i < 20; i++ {
		fmt.Println("Receiving:", <-ch)
	}
}

func Select(c chan int, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

// ch := make(chan int)
// 	quit := make(chan int)
// 	go func() {
// 		for i := 0; i < 10; i++ {
// 			fmt.Println(<-ch)
// 		}
// 		quit <- 0
// 	}()

// Select(ch, quit)

func Sync() {
	n := 0
	// Sử dụng sync.Mutex để đồng bộ hóa truy cập vào biến n
	var lock sync.Mutex
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1) // Thêm một goroutine vào WaitGroup
		go func() {
			defer wg.Done() // Đảm bảo goroutine này sẽ được đánh dấu là hoàn thành khi kết thúc
			for i := 0; i < 10000; i++ {
				// Sử dụng lock để đảm bảo chỉ một goroutine truy cập vào n tại một thời điểm
				lock.Lock()
				n++
				fmt.Println(n)
				// In giá trị của n sau khi tăng
				lock.Unlock()
			}

		}()

	}
	wg.Wait() // Chờ tất cả goroutines hoàn thành
	fmt.Println(n)
}
func MainConcurrency() {
	Sync()
}
