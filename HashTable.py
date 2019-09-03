class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value < v2.value:
            return -1
        elif v1.value > v2.value :
            return 1
        else:
            return 0
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def add(self, value):
        new_node = Node(value)
        if self.head == self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node is not None:
            if self.__ascending and self.compare(new_node, node) <= 0 or not self.__ascending and self.compare(
                    new_node, node) >= 0:
                if node.prev is None:
                    # Голова
                    new_node.next = node
                    node.prev = new_node
                    self.head = new_node
                else:
                    # Серединна
                    node.prev.next = new_node
                    new_node.prev = node.prev
                    new_node.next = node
                    node.prev = new_node
                return
            elif node.next is None:
                # Хвост
                node.next = new_node
                new_node.prev = node
                self.tail = new_node
                return
            node = node.next    
        # автоматическая вставка value 
        # в нужную позицию

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None # здесь будет ваш код

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
                if node == self.tail:
                    self.tail = node.prev
                    if self.tail is not None:
                        self.tail.next = None
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                node_pointer = node
                node = node.next
                del node_pointer
                return
            else:
                node = node.next
        return 'Удаляемого элемента не было'

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        pass # здесь будет ваш код

    def len(self):
        self.leng = 0
        if(self.head is None):
            return self.leng
        node = self.head
        while node is not None:
            node = node.next
            self.leng +=1
        return self.leng # здесь будет ваш код 

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.value.strip() < v2.value.strip():
            return -1
        elif v1.value.strip() > v2.value.strip():
            return 1
        else:
            return 0
        # переопределённая версия для строк