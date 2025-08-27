class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (float)):
            raise TypeError("Temperature must be a float")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

    @property
    def temperature_type(self):
        return "Celsius / Fahrenheit"
    
# 实例化对象
temp = Temperature(25.0)

# 测试属性访问
print(f"当前摄氏度: {temp.celsius}°C")           # 输出: 25°C
print(f"转换为华氏度: {temp.fahrenheit}°F")     # 输出: 77.0°F

# 测试华氏度设置
temp.fahrenheit = 100
print(f"新摄氏度: {temp.celsius:.1f}°C")        # 输出: 37.8°C

# 测试异常处理
try:
    temp.celsius = -300.0  # 触发ValueError
except ValueError as e:
    print(f"错误: {e}")  # 输出: 温度不能低于绝对零度

# 测试只读属性
print(temp.temperature_type)  # 输出: Celsius/Fahrenheit
temp.temperature_type = "K"   # 触发AttributeError