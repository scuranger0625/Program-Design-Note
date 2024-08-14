# 1. while 迴圈
# while 迴圈會在條件為 True 時不斷執行代碼塊。

counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1  # 必須更新 counter 以避免無限迴圈

# 注意事項：
# 1. 必須確保在迴圈內部有適當的邏輯來改變條件變數，否則可能會導致無限迴圈。
# 2. 可以選擇性地在 while 迴圈後加入 else 區塊，當條件變為 False 時執行。

# 2. for 迴圈
# for 迴圈用來遍歷序列（如列表、字符串等）的元素。

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 注意事項：
# 1. for 迴圈會遍歷序列中的每個元素，並且每個元素都會被賦值給迭代變數（如上例中的 fruit）。
# 2. for 迴圈也可以搭配 range() 函數來生成一系列數字進行迭代。

# 3. break 語句
# break 用來提前退出迴圈，不再執行剩餘的迴圈代碼。

for i in range(10):
    if i == 5:
        break  # 當 i 等於 5 時退出迴圈
    print(i)

# 注意事項：
# 1. break 通常與條件語句（如 if）搭配使用，用來在特定條件下跳出迴圈。
# 2. break 只能終止包含它的最近的迴圈。

# 4. continue 語句
# continue 用來跳過當前迴圈的剩餘代碼，直接進入下一次迭代。

for i in range(10):
    if i % 2 == 0:
        continue  # 當 i 為偶數時，跳過此次迭代
    print(i)

# 注意事項：
# 1. continue 通常與條件語句搭配使用，用來在特定條件下跳過當前迴圈的剩餘部分。
# 2. continue 不會終止迴圈，而是直接進入下一次迭代。

# 5. pass 語句
# pass 是一個空語句，什麼也不做。通常用來作為佔位符。

for i in range(5):
    if i < 3:
        pass  # 此處未實作邏輯，因此使用 pass 作為佔位符
    else:
        print(i)

# 注意事項：
# 1. pass 常用於結構完整性，如在函數或迴圈中尚未實作的部分。
# 2. 與註解不同，pass 是有效的 Python 語句，只是不會產生任何行為。
