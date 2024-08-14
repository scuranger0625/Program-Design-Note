# 1. 基本的檔案操作
# 在 Python 中，我們可以使用 open() 函數來打開檔案，並指定我們要進行的操作模式（如讀取或寫入）。

try:
    # 打開檔案進行讀取
    file = open("example.txt", "r")
    content = file.read()
    print("檔案內容:")
    print(content)
    
    # 打開檔案進行寫入
    file = open("example.txt", "w")
    file.write("這是一個新的內容")
    print("寫入完成")

except FileNotFoundError:
    print("檔案未找到，請確認檔案路徑")

except IOError:
    print("讀寫檔案時發生錯誤")

finally:
    file.close()
    print("檔案已關閉")

# 注意事項：
# 1. 使用 open() 函數打開檔案時，務必指定模式 ('r', 'w', 'a', 'b')，根據需求選擇讀取、寫入或附加。
# 2. 檔案操作完成後，必須使用 close() 函數來關閉檔案，以釋放系統資源。
# 3. 使用 try-except 結構來捕獲可能的檔案操作錯誤，例如檔案未找到 (FileNotFoundError) 或 IO 錯誤 (IOError)。

# 2. 使用 with 語句自動關閉檔案
# with 語句可以幫助我們自動管理資源，在操作完成後自動關閉檔案，避免手動關閉的麻煩。

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("使用 with 語句讀取的檔案內容:")
        print(content)

except FileNotFoundError:
    print("檔案未找到，請確認檔案路徑")

except IOError:
    print("讀寫檔案時發生錯誤")

# 注意事項：
# 1. 使用 with 語句可以自動處理檔案的開啟和關閉，確保資源不會泄露。
# 2. with 語句會在區塊內操作完成後自動調用 close() 方法，因此不需要顯式地關閉檔案。

# 3. 例外處理
# 在處理程式中可能會遇到各種例外狀況，例外處理可以幫助我們在這些情況下保持程式穩定性。

def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("錯誤: 不能除以零")
        return None
    except TypeError:
        print("錯誤: 請輸入數字")
        return None
    else:
        print("計算結果:", result)
        return result
    finally:
        print("計算完成")

# 測試例外處理
divide_numbers(10, 2)  # 正常情況
divide_numbers(10, 0)  # 觸發 ZeroDivisionError
divide_numbers(10, "a")  # 觸發 TypeError

# 注意事項：
# 1. 使用 try-except 語句來捕獲並處理可能的例外情況，防止程式崩潰。
# 2. except 區塊可以捕獲特定類型的例外，如 ZeroDivisionError 或 TypeError。
# 3. finally 區塊無論是否發生例外，最終都會執行，通常用於釋放資源或清理工作。
