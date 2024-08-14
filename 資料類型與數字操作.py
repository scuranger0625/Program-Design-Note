# 範例主題：資料類型與數字操作

# 1. 數字類型轉換
# Python 支援多種數字類型，包括整數、浮點數和複數。

# 整數轉換為浮點數
int_value = 10
float_value = float(int_value)
print("整數轉換為浮點數:", float_value)  # 輸出: 10.0

# 字串轉換為整數
str_value = "123"
int_value = int(str_value)
print("字串轉換為整數:", int_value)  # 輸出: 123

# 字串轉換為複數
complex_value = complex("1+2j")
print("字串轉換為複數:", complex_value)  # 輸出: (1+2j)

# 注意事項：
# 1. Python 允許使用 int()、float() 和 complex() 將不同的資料類型進行轉換。
# 2. 轉換字串時，確保字串內容能正確地解析為目標數字類型，否則會引發錯誤。


# 2. 浮點數運算與精度問題
# 浮點數運算可能會出現精度問題，這是由於大多數十進制浮點數不能精確地用二進制表示。

# 浮點數加法運算
result = 1.1 + 2.2
print("1.1 + 2.2 =", result)  # 輸出可能為: 3.3000000000000003

# 使用 decimal 模組進行精確計算
import decimal
a = decimal.Decimal('1.1')
b = decimal.Decimal('2.2')
result = a + b
print("使用 decimal 模組進行精確計算:", result)  # 輸出: 3.3

# 注意事項：
# 1. 浮點數運算時要注意精度問題，特別是在進行金融計算時。
# 2. 使用 decimal 模組可以進行精確的十進制浮點數運算，避免因二進制表示引起的精度問題。


# 3. 字串操作
# 字串是 Python 中的重要資料類型，可以使用單引號、雙引號或三引號定義字串。

# 字串定義
str1 = 'Hello'
str2 = "World"
str3 = """This is
a multiline
string"""

# 字串連接
full_str = str1 + " " + str2
print("字串連接:", full_str)  # 輸出: Hello World

# 字串索引和切片
print("第一個字元:", full_str[0])  # 輸出: H
print("切片操作:", full_str[1:5])  # 輸出: ello

# 使用 in 檢查子字串
print("'World' 是否在字串中:", "World" in full_str)  # 輸出: True

# 注意事項：
# 1. 字串是不可變的，這意味著一旦定義了字串，其內容就不能被修改。
# 2. 使用索引和切片可以獲取字串中的部分內容，且索引從 0 開始。
