package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"os"
)

func main() {

	outFile, err := os.Create("items.csv")
	if err != nil {
		log.Fatal(err)
	}

	data, err := ioutil.ReadFile("items.json")
	if err != nil {
		log.Fatal(err)
	}

	var documents []map[string]interface{}
	err = json.Unmarshal(data, &documents)
	if err != nil {
		log.Fatal(err)
	}

	headers := make([]string, 0, len(documents[0]))
	for header := range documents[0] {
		headers = append(headers, header)
		outFile.Write([]byte(header + ", "))
	}

	for _, document := range documents {
		for _, header := range headers {
			field, err := json.Marshal(document[header])
			if err != nil {
				log.Fatal(err)
			}
			outFile.Write(field) // Missing trailing comma
		}
	}

	log.Println("Number of documents", len(documents))

}
