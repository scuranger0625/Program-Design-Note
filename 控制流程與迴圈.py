# 1. 使用 if-else 判斷閏年
# 閏年：能被 4 整除但不能被 100 整除，或能被 400 整除的年份。

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是閏年")
else:
    print(f"{year} 不是閏年")

# 注意事項：
# 1. if-else 判斷可以根據條件執行不同的程式區塊。
# 2. `elif` 可以用來檢查多個條件。

# 2. 使用 for 迴圈生成九九乘法表
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()  # 用於分隔不同的乘法表

# 注意事項：
# 1. `for` 迴圈適用於遍歷序列（如列表、元組或字串）。
# 2. `range()` 函數用於生成數字序列，可以指定開始、結束和步長。

# 3. 使用 while 迴圈尋找 2 到 10000000 之間的質數
start = 2
end = 100
prime_numbers = []

while start <= end:
    is_prime = True
    for i in range(2, int(start ** 0.5) + 1):
        if start % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(start)
    start += 1

print("質數:", prime_numbers)

# 注意事項：
# 1. `while` 迴圈在條件為 True 時不斷執行，適合用於需要重複執行的操作。
# 2. 小心無限迴圈，確保在每次迴圈後有機會讓條件變為 False。

# 4. 使用 continue 與 break 控制迴圈
numbers = range(1, 10)

for num in numbers:
    if num % 2 == 0:
        continue  # 跳過偶數
    print(num)

    if num == 7:
        break  # 當數字為 7 時結束迴圈

# 注意事項：
# 1. `continue` 用於跳過當前迭代的剩餘部分，進入下一次迭代。
# 2. `break` 用於終止整個迴圈。

# 5. 使用 pass 作為佔位符
for num in numbers:
    if num % 2 == 0:
        pass  # 這裡什麼也不做，但保留程式結構
    else:
        print(f"奇數: {num}")

# 注意事項：
# 1. `pass` 是一個空語句，當你需要在語法上需要一個語句但不想執行任何動作時使用。
# 2. `pass` 常用於構建空函數、迴圈或條件結構，以保留程式的完整性。
