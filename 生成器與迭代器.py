# 1. 迭代器的使用
# 迭代器是一種可以一次返回一個元素的對象。通常通過實現 __iter__() 和 __next__() 方法來創建。

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# 創建並使用迭代器
my_iter = MyIterator(1, 5)
for number in my_iter:
    print(number)

# 注意事項：
# 1. 迭代器通過 __iter__() 返回自身以便迭代，__next__() 用於獲取下一個元素。
# 2. 當沒有更多元素時，__next__() 應該引發 StopIteration 來終止迭代。

# 2. 生成器的使用
# 生成器是一種更簡單的方式來創建迭代器。它使用 yield 關鍵字來產生值，每次暫停和恢復函數的執行。

def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# 使用生成器
for number in my_generator(1, 5):
    print(number)

# 注意事項：
# 1. 生成器函數在每次調用 yield 時暫停並保存其狀態，下次被調用時從保存的狀態恢復。
# 2. 生成器比手動實現迭代器簡單且更高效，特別是在處理大型數據集或無限序列時。

# 3. 無限迭代器的例子
# 無限迭代器可以通過避免設置終止條件來創建。

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# 使用無限迭代器（需要小心使用以避免無限循環）
# for number in infinite_counter():
#     print(number)

# 注意事項：
# 1. 無限迭代器可以用於需要無限數據流的場景，如伺服器請求處理，但需謹慎使用避免卡住系統。
# 2. 可以手動停止迭代以防止無限循環。

# 4. 使用生成器處理大數據集
# 當處理大數據集時，生成器可以幫助節省記憶體，因為它們一次只生成一個元素。

def large_dataset_generator(n):
    for i in range(n):
        yield i * i

# 迭代大數據集
for value in large_dataset_generator(1000000):
    if value > 100:
        break
    print(value)

# 注意事項：
# 1. 生成器僅在需要時生成值，因此在處理大數據或無限數據流時特別有用。
# 2. 使用生成器可以顯著減少記憶體使用，因為它不會將所有數據一次性存儲在記憶體中。
