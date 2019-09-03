class HashTable:
    def __init__(self, sz, stp):
        self.size = sz #размер хэш-таблицы
        self.step = stp # длиннa шага (количество слотов)
        self.slots = [None] * self.size

    def hash_fun(self, value):
        val = str(value) # в качестве value поступают строки!
        index = 0
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i + 1)
            elif int(val) == 0:
                index = 0
                return index
            else:
                index += 2 * (i + 1)
        if self.size != 0:
            index = index % self.size
        return index   
         # всегда возвращает корректный индекс слота
    def seek_slot(self, value): # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        x = self.size - 1
        if x == 0:
            if self.slots[index] is None:
                return index
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            else:
                index += self.step
                while index > x:
                    if x == 0:
                        index -= 1
                    index -= x
                if self.slots[index] is None:
                    return index
        return None

    def put(self, value):         
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value
            return x
        else:
            return None
    def find(self, value):
        index = self.hash_fun(value)
        x = self.size - 1
        if x == 0:
            if self.slots[index] is value:
                return index
        for i in range(self.size):
            if self.slots[index] is value:
                return index
            else:
                index += self.step
                while index > x:
                    index -= x
                    if x == 0:
                        index -= x
        return None

s1 = HashTable(17, 3)
for i in range(30,70):
    s1.put(i)
print('find - ',s1.find(46))
print(s1.put(0), s1.slots, s1.size, len(s1.slots))