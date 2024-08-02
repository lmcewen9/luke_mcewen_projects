package main

import (
	"fmt"
	"strconv"
)

type Node struct {
	value int
	next  *Node
}

type LinkedList struct {
	size  int
	index int
	head  *Node
}

func (list *LinkedList) Append(item int) {
	var newNode *Node = &Node{value: item, next: nil}
	if list.head == nil {
		newNode.next = list.head
		list.head = newNode
	} else {
		tmp := list.head
		for tmp.next != nil {
			tmp = tmp.next
		}
		tmp.next = newNode

	}
	list.size++

}

func (list *LinkedList) TextOutput() string {
	tmp := list.head
	var ret string = "["
	for tmp != nil {
		if tmp.next == nil {
			ret += strconv.Itoa(tmp.value)
			break
		}
		ret += strconv.Itoa(tmp.value) + ", "
		tmp = tmp.next

	}
	return ret + "]"
}

func main() {
	var list *LinkedList = &LinkedList{size: 0, index: 0, head: nil}
	list.Append(1)
	list.Append(2)
	list.Append(3)
	list.Append(4)
	fmt.Println(list.TextOutput())

}
