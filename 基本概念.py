# 1. 基本概念示例

# 打印 "Hello, World!" 到控制台
# Python 的入門程式
print("Hello, World!")

# 注意事項：
# 1. `print()` 是 Python 中最基本的輸出函數，用於將訊息打印到控制台。
# 2. Python 使用縮排來表示程式區塊，而不是使用大括號 `{}`。

# 2. Python 的不同實現版本示例

# CPython 是 Python 的經典實現
# Jython, IronPython, 和 PyPy 是 Python 的不同實現版本

# 示例：在 PyPy 上運行代碼以提高性能
import time

def long_running_task():
    """模擬一個耗時操作"""
    start_time = time.time()
    total = 0
    for i in range(1, 1000000):
        total += i
    end_time = time.time()
    print(f"計算結果：{total}, 耗時：{end_time - start_time:.2f} 秒")

# 執行長時間運行的任務
# 如果使用 PyPy 來運行這段代碼，通常會顯著減少執行時間
long_running_task()

# 注意事項：
# 1. CPython 是最常用的 Python 實現，適用於大多數應用場景。
# 2. PyPy 通常能夠顯著提高計算密集型任務的運行速度，適合需要高性能的應用。
# 3. Jython 和 IronPython 適合與 Java 和 .NET 集成的場景。

# 3. Python 開發環境示例

# Python 支援多種開發環境，如 IDLE, Anaconda, Visual Studio Code, PyCharm 等
# 這裡我們展示如何使用 Visual Studio Code 進行開發

# 在 Visual Studio Code 中，你可以使用以下命令來安裝 Python 擴展：
# 打開 VS Code 的命令行工具，輸入以下指令來安裝 Python 擴展包
# (此命令需在命令行中運行，而非 Python 程式碼內)
# code --install-extension ms-python.python

# 注意事項：
# 1. IDLE 是 Python 的內建開發環境，適合初學者使用。
# 2. Anaconda 是一個適合資料科學和機器學習的 Python 平台，包含了多種科學計算庫。
# 3. Visual Studio Code 是一個輕量級的編輯器，支援多種語言和擴展，是目前流行的開發工具之一。
# 4. PyCharm 是一個功能強大的 Python 專業開發環境，適合進行大型項目開發。
