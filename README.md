# pixelPackages3D

 [English](.\README_EN.md) | 简体中文

pixelPackages3D 是一个最简3D封装生成库，包含模型的总体轮廓数据，基于[FreeCAD](https://www.freecad.org/)的参数表完成，去除3D模型的细节并最后使用`stepreduce.exe`减小模型的大小。

## Resistor_SMD - 贴片电阻

### Standard_Resistor_SMD.FCStd

标准封装的电阻封装库，输出步骤如下：

1. 调用 `Standard_Resistor_SMD.FCMacro` 宏命令完成多组模型的原始 step 文件输出。
2. 使用`python stepreduce.py ./Resistor_SMD/ ./Resistor_SMD/Standard_Resistor_SMD/`调用 `stepreduce.exe` 完成 step 模型压缩

## Capacitor_SMD - 贴片电容

### Standard_Capacitor_SMD.FCStd

标准封装的电阻封装库，输出步骤如下：

1. 调用 `Standard_Capacitor_SMD.FCMacro` 宏命令完成多组模型的原始 step 文件输出。
2. 使用`python stepreduce.py ./Capacitor_SMD/ ./Capacitor_SMD/Standard_Capacitor_SMD/`调用 `stepreduce.exe` 完成 step 模型压缩


## 致谢

- <https://gitlab.com/kicad/libraries/kicad-packages3D-source>
- <https://gitlab.com/sethhillbrand/stepreduce>
