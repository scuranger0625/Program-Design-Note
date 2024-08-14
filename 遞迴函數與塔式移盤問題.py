# 1. 遞迴函數
# 遞迴函數是指在函數內部調用自身的函數。這種方法適合解決分解為更小問題的問題，如塔式移盤問題。

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"將圓盤從 {source} 移到 {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"將圓盤從 {source} 移到 {target}")
    hanoi(n-1, auxiliary, target, source)

# 執行塔式移盤問題
n = 3  # 假設有 3 個圓盤
hanoi(n, 'A', 'C', 'B')

# 注意事項：
# 1. 遞迴函數必須有一個基礎情況來停止遞迴（即當 n == 1 時）。
# 2. 遞迴的每一步都在解決一個更小的子問題，最終解決整個問題。
# 3. 遞迴可能會導致大量的調用堆疊，因此在處理非常大的數據集或需要高效能時要謹慎。

# 2. 計算步驟數
# 我們還可以計算移動所有圓盤所需的步驟數。

def hanoi_steps(n):
    if n == 1:
        return 1
    return 2 * hanoi_steps(n-1) + 1

# 計算 3 個圓盤所需的步驟數
steps = hanoi_steps(n)
print(f"將 {n} 個圓盤從 A 移到 C 需要 {steps} 步驟")

# 注意事項：
# 1. 步驟數可以通過公式 2^n - 1 直接計算，這也是遞迴的結果。
# 2. 使用遞迴計算步驟數展示了遞迴的靈活性，即使問題規模變化，遞迴仍然適用。

# 3. 從使用者輸入讀取圓盤數
# 我們可以從使用者輸入讀取需要移動的圓盤數。

n = int(input("請輸入圓盤數量: "))
hanoi(n, 'A', 'C', 'B')

# 注意事項：
# 1. 使用 input() 函數從使用者獲取輸入，記得將其轉換為整數型別以進行數學運算。
# 2. 保持使用者介面簡單且直觀，提示輸入必須符合預期格式（如整數）。

