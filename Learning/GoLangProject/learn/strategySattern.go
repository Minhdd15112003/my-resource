package main

import (
	"fmt"
)

// type là một kiểu dữ liệu tùy chỉnh, có thể chứa các trường và phương thức
// struct là một kiểu dữ liệu phức hợp trong Go, cho phép bạn nhóm các trường dữ liệu lại với nhau
// interface là một tập hợp các phương thức mà một kiểu dữ liệu phải thực hiện
// nil là một giá trị đặc biệt trong Go, đại diện cho một con trỏ không trỏ đến bất kỳ giá trị nào
// Bước 1: Định nghĩa interface cho Strategy
type NotiStrategy interface {
	Send(msg string) error
}

// Bước 2: Triển khai các Strategy cụ thể
// Strategy 1: Gửi thông báo qua Email
type EmailNoti struct{}

func (e EmailNoti) Send(msg string) error {
	fmt.Printf("Gửi email: %s\n", msg)
	return nil
}

// Strategy 2: Gửi thông báo qua SMS
type SMSNoti struct{}

func (s SMSNoti) Send(msg string) error {
	fmt.Printf("Gửi SMS: %s\n", msg)
	return nil
}

// Bước 3: Tạo Context để sử dụng Strategy
type Notifier struct {
	strategy NotiStrategy
}

// Phương thức để thay đổi Strategy tại runtime
func (n *Notifier) SetStrategy(strategy NotiStrategy) {
	n.strategy = strategy
}

// Phương thức để gửi thông báo sử dụng Strategy hiện tại
func (n *Notifier) SendNoti(msg string) error {
	return n.strategy.Send(msg)
}

func MainNoti() {
	notifier := &Notifier{}

	notifier.SetStrategy(EmailNoti{})
	notifier.SendNoti("EmailNoti")
}
