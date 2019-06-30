package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

const jsonuri = "https://x/aws-master-org.json"

// Account struct
type Account struct {
	OU      string `json:"ou"`
	ID      string `json:"id"`
	Account string `json:"account"`
}

func main() {
	// download json
	resp, err := http.Get(jsonuri)
	fmt.Println(resp.Body, err)
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	// fmt.Printf("%s", body)

	// parse test with json data
	// example := []byte(`{"ou": "auto", "id": "x", "account": "x"}`)
	// fmt.Println(example)

	// var acc1 Account
	// json.Unmarshal(example, &acc1)
	// fmt.Println(acc1)
	// fmt.Println(acc1.ID)

	// parse test2 with json data in list
	// example := []byte(`[{"ou": "auto", "id": "x", "account": "x"},{"ou": "auto", "id": "x", "account": "x"}]`)
	// fmt.Println(example)

	// accountlist := make([]Account, 0)
	// json.Unmarshal(example, &accountlist)
	// fmt.Println(accountlist)

	// parse json
	accountlist := make([]Account, 0)
	fmt.Println(accountlist)
	err = json.Unmarshal(body, &accountlist)
	if err != nil {
		panic(err)
	}
	fmt.Println(accountlist)
	for i, v := range accountlist {
		fmt.Println(i, v.Account)
	}

}
