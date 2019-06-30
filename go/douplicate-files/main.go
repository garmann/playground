package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
)

const path = "/foobar"

func fileHash(path string) (string, error) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	hash_binary := md5.New()
	_, err = io.Copy(hash_binary, file)
	if err != nil {
		log.Fatal(err)
	}

	hashbytes := hash_binary.Sum(nil)
	hash := hex.EncodeToString(hashbytes)
	//fmt.Printf("%x", hash_binary.Sum(nil))
	return hash, err
}

type FileInfo struct {
	Hash string
	Path string
}

func main() {
	files := make(map[string][]string)

	err := filepath.Walk(path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() == true {
			return nil
		}

		hash, err := fileHash(path)
		if err != nil {
			return err
		}

		//fmt.Println(hash)
		// hashinfo := make(map[string]HashInfo)
		// hashinfo[hash]
		// hashinfo := FileInfo{Hash: hash, Path: path}
		//fmt.Println(hashinfo)

		files[hash] = append(files[hash], path)

		return nil
	})
	if err != nil {
		log.Println(err)
	}

	for k, v := range files {
		if len(v) > 1 {
			fmt.Println("k:", k, "v:", v)
			fmt.Println("len slice:", len(v))
			fmt.Println("deleting file:", v[0])
			err := os.Remove(v[0])
			if err != nil {
				fmt.Println("there was an error", err)
			}
			fmt.Println("")

		}
	}
}
