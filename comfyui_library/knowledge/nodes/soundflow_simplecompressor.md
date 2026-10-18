# SoundFlow_SimpleCompressor

## 节点类型

`SoundFlow_SimpleCompressor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `threshold_db:FLOAT`（1 次）
- `ratio:FLOAT`（1 次）
- `attack_ms:FLOAT`（1 次）
- `release_ms:FLOAT`（1 次）
- `knee_db:FLOAT`（1 次）
- `makeup_gain_db:FLOAT`（1 次）
- `mix:FLOAT`（1 次）

## 输出

- `AUDIO:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-20, 4, 10, 100, 0, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
