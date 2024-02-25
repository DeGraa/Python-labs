import time
import math


def invoke_after_ms(num, ms):
    time.sleep(ms / 1000)
    print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")


num = int(input())
ms = int(input())
invoke_after_ms(num, ms)
