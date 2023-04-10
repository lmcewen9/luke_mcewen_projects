class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    
    def __str__(self):
        return str(self.value)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next != None:
            return self.next
        else:
            print("exception raised")
            try:
                raise StopIteration
            except:
                pass

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.index = 0
    
    def __str__(self):
        tmp = self.head
        _str = "["
        while (tmp != None):
            if tmp.next == None:
                _str += str(tmp.value)
                break
            _str += str(tmp.value) + ", "
            tmp = tmp.next
        _str += "]"
        return _str
    
    def __iter__(self):
        return self
    
    def __next__(self):
        tmp = self.head
        count = 0
        while count < self.index:
            tmp = tmp.next
            count += 1
        self.index += 1
        if self.index <= self.size:
            if self.index == 1:
                return self.head
            return tmp
        else:
            raise StopIteration
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, item):
        if item < 0:
            return "can't index a negative value..."
        tmp = self.head
        index = 0
        while(index < item):
            try:
                tmp = tmp.next
            except:
                return "Index out of range..."
            index += 1
        return tmp

    def add(self, value):
        new_node = Node(value)
        if self.size == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp = self.head
            while (tmp.next!= None):
                tmp = tmp.next
            tmp.next = new_node
        self.size += 1


    def delete_value(self, value):
        if self.size == 0:
            print("Index out of range...")
        tmp = self.head
        try:
            while(tmp.next.value != value):
                tmp = tmp.next
            tmp.next = tmp.next.next
            self.size -= 1
        except:
            print("value not in list...")

    def delete_index(self, index):
        if index < 0:
            print("Cant delete at a negative index...")
            return
        elif self.size-1 < index or self.size == 0:
            print("Index out of range...")
            return
        tmp = self.head
        count = 0
        while(count < index-1):
            tmp = tmp.next
            count += 1
        tmp.next = tmp.next.next
        self.size -= 1

def main():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    #print(linked_list)
    #linked_list.delete_value(2)
    #print(linked_list)
    linked_list.add("Luke")
    linked_list.add(69)
    #print(linked_list)
    #linked_list.delete_index(3)
    #print(linked_list)
    #for i in linked_list:
    #    print(i)
    #for i in range(len(linked_list)):
    #    print(linked_list[i])

if __name__ == "__main__":
    main()