# OpenMAIC_音频混音

## 节点类型

`OpenMAIC_音频混音`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `讲解音频:STRING`（1 次）
- `背景音乐:STRING`（1 次）
- `讲解音量:INT`（1 次）
- `BGM音量:INT`（1 次）
- `循环BGM:BOOLEAN`（1 次）

## 输出

- `混音音频:STRING`（1 次）
- `时长:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 0, -18, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
