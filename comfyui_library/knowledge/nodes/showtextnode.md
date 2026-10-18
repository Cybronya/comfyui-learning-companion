# ShowTextNode

## 节点类型

`ShowTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `sense_voice_output:TEXT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["<|zh|><|NEUTRAL|><|Speech|><|woitn|>这是一个关于声音的测试我在使用一个软件把我的声音作为输出项"]`（1 次）
- `["<|zh|><|NEUTRAL|><|Speech|><|woitn|>hello 大家好今天我们起来看一个对口型的工作流"]`（1 次）
- `["<|zh|><|NEUTRAL|><|Speech|><|woitn|>尾巴不只能用来挠痒痒哦", [false, true]]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
