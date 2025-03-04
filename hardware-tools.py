import platform
from cpuinfo import get_cpu_info

# 确认架构 AMD64
print(platform.machine())

# 返回处理器名称，可能显示 Intel 相关信息，Intel64 Family 6 Model 94 Stepping 3, GenuineIntel
print(platform.processor())

# 显示具体的 CPU 品牌和型号，Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz
info = get_cpu_info()
print(info['brand_raw'])