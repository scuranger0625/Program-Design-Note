# 1. 定義類別與物件屬性
# 在 Python 中，我們可以使用 class 關鍵字來定義一個類別。類別是物件的藍圖或範本。

class Parrot:
    # 類別屬性
    species = "bird"

    # 初始化方法 (Constructor)
    def __init__(self, name, age):
        # 實例屬性
        self.name = name
        self.age = age

    # 方法 (行為)
    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# 創建類別的實例（物件）
parrot1 = Parrot("Blue", 10)
parrot2 = Parrot("Green", 15)

# 訪問類別屬性
print(f"{parrot1.name} is a {parrot1.__class__.species}")  # 輸出: Blue is a bird

# 訪問實例屬性
print(f"{parrot2.name} is {parrot2.age} years old")  # 輸出: Green is 15 years old

# 呼叫方法
print(parrot1.sing("Happy"))  # 輸出: Blue sings Happy
print(parrot2.dance())  # 輸出: Green is now dancing

# 注意事項：
# 1. `__init__` 是一個特殊方法，用來初始化新的物件。這個方法在物件創建時自動調用。
# 2. 類別屬性是所有物件共享的，而實例屬性則是每個物件獨立擁有的。

# 2. 繼承 (Inheritance)
# 繼承允許我們基於已有的類別來創建新類別，從而可以重用代碼。

class FlyingParrot(Parrot):
    def fly(self):
        return f"{self.name} can fly"

# 創建子類的實例
parrot3 = FlyingParrot("Sky", 3)

# 訪問繼承的屬性和方法
print(parrot3.fly())  # 輸出: Sky can fly
print(parrot3.sing("Wonder"))  # 輸出: Sky sings Wonder

# 注意事項：
# 1. 子類會繼承父類的所有屬性和方法，但可以覆蓋或擴展它們。
# 2. 使用 `super()` 可以在子類中調用父類的方法。

# 3. 封裝 (Encapsulation)
# 封裝是將對象的內部狀態和行為保護起來，使外界無法直接訪問它們。

class EncapsulatedParrot:
    def __init__(self, name, age):
        self.__name = name  # 私有屬性
        self.__age = age

    def get_info(self):
        return f"{self.__name} is {self.__age} years old"

# 創建封裝類的實例
parrot4 = EncapsulatedParrot("Secret", 5)

# 訪問私有屬性（會導致錯誤）
# print(parrot4.__name)  # AttributeError: 'EncapsulatedParrot' object has no attribute '__name'

# 使用公開方法訪問私有屬性
print(parrot4.get_info())  # 輸出: Secret is 5 years old

# 注意事項：
# 1. 使用雙下劃線 `__` 開頭的屬性是私有的，不能從類外部直接訪問。
# 2. 可以使用公開方法來訪問或修改私有屬性，這樣可以保護對象的內部狀態。

# 4. 多型 (Polymorphism)
# 多型允許我們用相同的介面來處理不同類型的對象。

class Bird:
    def intro(self):
        return "There are many types of birds."

    def flight(self):
        return "Most of the birds can fly."

class Penguin(Bird):
    def flight(self):
        return "Penguins do not fly."

# 創建實例
bird = Bird()
penguin = Penguin()

# 多型：不同對象使用相同的方法名，但表現不同
print(bird.intro())  # 輸出: There are many types of birds.
print(bird.flight())  # 輸出: Most of the birds can fly.
print(penguin.intro())  # 輸出: There are many types of birds.
print(penguin.flight())  # 輸出: Penguins do not fly.

# 注意事項：
# 1. 多型允許我們使用相同的方法來處理不同類型的對象，這使得代碼更具靈活性和可擴展性。
# 2. 在 Python 中，多型主要通過方法覆蓋 (method overriding) 來實現。
