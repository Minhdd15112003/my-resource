package main

import (
	"fmt"
)

func plus(a int, b int) int {
	return a + b
}

func swap(x, y string) (string, string) {
	return y, x
}
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func sumUseFor(sum int) int {
	for i := 0; i < 10; i++ {
		print(i)
		sum += i
	}
	return sum
}
func sumUseWhile(sum int) int {
	for sum < 10 {
		print(sum)
		print("\n")
		sum += sum
		if sum <= 0 {
			print("khong so nho hon khong duoc")
			break
		}
	}

	return sum
}
func forRange() {
	numbers := []int{1, 2, 3, 4, 5}
	// Lấy cả index và value
	for i, v := range numbers {
		fmt.Printf("Index: %d, Value: %d\n", i, v)
	}

	// Chỉ lấy value (bỏ qua index)
	for _, v := range numbers {
		fmt.Printf("Value: %d\n", v)
	}

	// Chỉ lấy index (bỏ qua value)
	for i := range numbers {
		fmt.Printf("Index: %d\n", i)
	}
}
func switchCase(number int) {
	switch number {
	case 1:
		print("case 1")

	case 2:
		print("case 2")

	default:
		print("defaut")
	}
}
func deferr() {
	//defer sẽ chạy cuối cùng trong một hàm
	defer fmt.Print("world ")
	fmt.Print("Hello")
}
func pointer() {
	//&biến: Lấy địa chỉ của biến.
	//*con_trỏ: Truy cập giá trị tại địa chỉ mà con trỏ trỏ đến.
	i, j := 10, 20
	p := &i
	print(*p)
	*p = 11
	print(i)

	p = &j
	*p = *p / 2
	print(j)
}

type Cat struct {
	Name   string
	Age    int
	gender string
}

func structs() {

	c := Cat{"moi", 2, "nam"}
	fmt.Print(c)

}
func array() {
	var a [2]string
	a[0] = "cac "
	a[1] = "to"

	fmt.Print(a)
}

func slice() {
	s := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	s = s[1:5]
	fmt.Print(s)

	// chạy đến phần tử thứ 2 và 3
	s = s[:2]
	fmt.Print(s)

	// chạy đến cuối slice
	s = s[0:]
	fmt.Print(s)

	//auto gen slice
	a := make([]int, 0, 5)
	a = append(a, 1, 2, 3, 4, 5, 6)
	fmt.Print(a)
}

// interface
type ManamentCat interface {
	AddAge(number int) Cat
}

// method
func (c *Cat) AddAge(number int) Cat {
	c.Age += number
	return *c
}

func (c *Cat) InfoCat() string {
	return fmt.Sprint(c.Name, c.Age, c.gender)
}

// Generics
func genericsAndMap() {
	// Map lưu điểm số của học sinh
	scores := make(map[string]map[string]float64) // Map lồng nhau: student -> subject -> score

	// Thêm điểm số
	scores["Alice"] = map[string]float64{
		"Math":    90.5,
		"English": 85.0,
	}
	scores["Bob"] = map[string]float64{
		"Math":    95.0,
		"English": 88.0,
	}

	// Truy xuất điểm số
	fmt.Println("Alice's Math score:", scores["Alice"]["Math"]) // Output: 90.5

	// Duyệt qua tất cả học sinh và điểm
	for student, subjects := range scores {
		fmt.Printf("Student: %s\n", student)
		for subject, score := range subjects {
			fmt.Printf("  %s: %.1f\n", subject, score)
		}
	}
	fmt.Println(scores) // Output: 90.5
}

func main() {
	genericsAndMap()
}
