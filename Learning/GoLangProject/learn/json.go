package main

import (
	"encoding/json"
	"log"
	"time"
)

type TodoItem struct {
	Id          string     `json:"id"`
	Title       string     `json:"title"`
	Description string     `json:"description"`
	Status      string     `json:"status"`
	CreatedAt   *time.Time `json:"created_at"`
	UpdatedAt   *time.Time `json:"updated_at,omitempty"`
}

// omitempty sẽ loại bỏ trường nếu giá trị nil
func Json() {
	now := time.Now().UTC()
	item := TodoItem{
		Id:          "2342342343",
		Title:       "Task",
		Description: "Conten 1",
		Status:      "Doing",
		CreatedAt:   &now,
		UpdatedAt:   &now,
	}
	//encoding struct to json dưới dạng byte
	jsData, err := json.MarshalIndent(item, "", "  ")
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(string(jsData))

	// giải mã từ json thành struct
	jsString := "{\"id\":\"2342342343\",\"title\":\"Task\",\"description\":\"Conten 1\",\"status\":\"Doing\",\"created_at\":\"2025-07-31T13:16:52.507667904Z\",\"updated_at\":\"2025-07-31T13:16:52.507667904Z\"}"
	var item2 TodoItem
	if err := json.Unmarshal([]byte(jsString), &item2); err != nil {
		log.Fatalln(err)
	}
	log.Println(item2)
}
