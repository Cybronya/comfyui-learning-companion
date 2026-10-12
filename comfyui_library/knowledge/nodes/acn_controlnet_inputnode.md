# ACN_ControlNet++InputNode

## 节点类型

`ACN_ControlNet++InputNode`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prev_plus_input:PLUS_INPUT`（2 次）

## 输出

- `PLUS_INPUT:PLUS_INPUT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["inpaint/outpaint"]`（1 次）
- `["segment"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
