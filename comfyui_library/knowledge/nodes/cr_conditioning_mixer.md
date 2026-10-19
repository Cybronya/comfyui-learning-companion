# CR Conditioning Mixer

## 节点类型

`CR Conditioning Mixer`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `conditioning_1:CONDITIONING`（2 次）
- `conditioning_2:CONDITIONING`（2 次）
- `mix_method:COMBO`（2 次）
- `average_strength:FLOAT`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Combine", 0.5]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
