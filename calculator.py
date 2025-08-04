#!/usr/bin/env python3
"""
Python控制台计算器程序
支持基本数学运算：加、减、乘、除、幂运算、平方根等
"""

import math
import sys
from typing import Union, Optional

class Calculator:
    """计算器类，提供各种数学运算功能"""
    
    def __init__(self):
        self.history = []  # 计算历史记录
        self.memory = 0    # 内存存储
    
    def add(self, a: float, b: float) -> float:
        """加法运算"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """减法运算"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """乘法运算"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """除法运算"""
        if b == 0:
            raise ValueError("错误：除数不能为零！")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """幂运算"""
        result = math.pow(base, exponent)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, number: float) -> float:
        """平方根运算"""
        if number < 0:
            raise ValueError("错误：不能计算负数的平方根！")
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """阶乘运算"""
        if n < 0:
            raise ValueError("错误：阶乘不能用于负数！")
        if n > 20:
            raise ValueError("错误：阶乘数值过大，请输入20以内的整数！")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def sin(self, angle: float) -> float:
        """正弦函数（弧度）"""
        result = math.sin(angle)
        self.history.append(f"sin({angle}) = {result}")
        return result
    
    def cos(self, angle: float) -> float:
        """余弦函数（弧度）"""
        result = math.cos(angle)
        self.history.append(f"cos({angle}) = {result}")
        return result
    
    def tan(self, angle: float) -> float:
        """正切函数（弧度）"""
        result = math.tan(angle)
        self.history.append(f"tan({angle}) = {result}")
        return result
    
    def log(self, number: float, base: float = 10) -> float:
        """对数运算"""
        if number <= 0:
            raise ValueError("错误：对数的真数必须为正数！")
        if base <= 0 or base == 1:
            raise ValueError("错误：对数的底数必须为正数且不等于1！")
        result = math.log(number, base)
        self.history.append(f"log_{base}({number}) = {result}")
        return result
    
    def ln(self, number: float) -> float:
        """自然对数"""
        if number <= 0:
            raise ValueError("错误：自然对数的真数必须为正数！")
        result = math.log(number)
        self.history.append(f"ln({number}) = {result}")
        return result
    
    def clear_history(self):
        """清空计算历史"""
        self.history.clear()
        print("计算历史已清空！")
    
    def show_history(self):
        """显示计算历史"""
        if not self.history:
            print("暂无计算历史")
            return
        print("\n=== 计算历史 ===")
        for i, record in enumerate(self.history[-10:], 1):  # 只显示最近10条
            print(f"{i}. {record}")
        print("================")
    
    def set_memory(self, value: float):
        """设置内存值"""
        self.memory = value
        print(f"内存已设置为: {value}")
    
    def get_memory(self) -> float:
        """获取内存值"""
        return self.memory
    
    def clear_memory(self):
        """清空内存"""
        self.memory = 0
        print("内存已清空！")

def get_number_input(prompt: str) -> float:
    """获取用户输入的数字"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("错误：请输入有效的数字！")

def get_operation() -> str:
    """获取用户选择的运算"""
    print("\n=== 可用运算 ===")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 幂运算 (^)")
    print("6. 平方根 (√)")
    print("7. 阶乘 (!)")
    print("8. 正弦 (sin)")
    print("9. 余弦 (cos)")
    print("10. 正切 (tan)")
    print("11. 对数 (log)")
    print("12. 自然对数 (ln)")
    print("13. 显示历史")
    print("14. 清空历史")
    print("15. 设置内存")
    print("16. 获取内存")
    print("17. 清空内存")
    print("0. 退出")
    print("================")
    
    return input("请选择运算 (0-17): ").strip()

def main():
    """主函数"""
    calc = Calculator()
    
    print("欢迎使用Python控制台计算器！")
    print("输入 'help' 查看帮助，输入 'quit' 退出程序")
    
    while True:
        try:
            choice = get_operation()
            
            if choice == '0' or choice.lower() in ['quit', 'exit', 'q']:
                print("感谢使用！再见！")
                break
            
            elif choice == '13':
                calc.show_history()
                continue
            
            elif choice == '14':
                calc.clear_history()
                continue
            
            elif choice == '15':
                value = get_number_input("请输入要存储的值: ")
                calc.set_memory(value)
                continue
            
            elif choice == '16':
                print(f"内存中的值: {calc.get_memory()}")
                continue
            
            elif choice == '17':
                calc.clear_memory()
                continue
            
            elif choice == '1':  # 加法
                a = get_number_input("请输入第一个数: ")
                b = get_number_input("请输入第二个数: ")
                result = calc.add(a, b)
                print(f"结果: {a} + {b} = {result}")
            
            elif choice == '2':  # 减法
                a = get_number_input("请输入第一个数: ")
                b = get_number_input("请输入第二个数: ")
                result = calc.subtract(a, b)
                print(f"结果: {a} - {b} = {result}")
            
            elif choice == '3':  # 乘法
                a = get_number_input("请输入第一个数: ")
                b = get_number_input("请输入第二个数: ")
                result = calc.multiply(a, b)
                print(f"结果: {a} * {b} = {result}")
            
            elif choice == '4':  # 除法
                a = get_number_input("请输入被除数: ")
                b = get_number_input("请输入除数: ")
                result = calc.divide(a, b)
                print(f"结果: {a} / {b} = {result}")
            
            elif choice == '5':  # 幂运算
                base = get_number_input("请输入底数: ")
                exponent = get_number_input("请输入指数: ")
                result = calc.power(base, exponent)
                print(f"结果: {base} ^ {exponent} = {result}")
            
            elif choice == '6':  # 平方根
                number = get_number_input("请输入要计算平方根的数: ")
                result = calc.sqrt(number)
                print(f"结果: √{number} = {result}")
            
            elif choice == '7':  # 阶乘
                n = int(get_number_input("请输入要计算阶乘的整数: "))
                result = calc.factorial(n)
                print(f"结果: {n}! = {result}")
            
            elif choice == '8':  # 正弦
                angle = get_number_input("请输入角度（弧度）: ")
                result = calc.sin(angle)
                print(f"结果: sin({angle}) = {result}")
            
            elif choice == '9':  # 余弦
                angle = get_number_input("请输入角度（弧度）: ")
                result = calc.cos(angle)
                print(f"结果: cos({angle}) = {result}")
            
            elif choice == '10':  # 正切
                angle = get_number_input("请输入角度（弧度）: ")
                result = calc.tan(angle)
                print(f"结果: tan({angle}) = {result}")
            
            elif choice == '11':  # 对数
                number = get_number_input("请输入真数: ")
                base = get_number_input("请输入底数 (默认10): ")
                result = calc.log(number, base)
                print(f"结果: log_{base}({number}) = {result}")
            
            elif choice == '12':  # 自然对数
                number = get_number_input("请输入真数: ")
                result = calc.ln(number)
                print(f"结果: ln({number}) = {result}")
            
            else:
                print("无效的选择，请重新输入！")
                
        except ValueError as e:
            print(f"错误: {e}")
        except KeyboardInterrupt:
            print("\n程序被中断，再见！")
            break
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()