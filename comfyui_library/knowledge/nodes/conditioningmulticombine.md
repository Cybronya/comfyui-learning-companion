# ConditioningMultiCombine

## 节点类型

`ConditioningMultiCombine`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `conditioning_1:CONDITIONING`（4 次）
- `conditioning_2:CONDITIONING`（4 次）
- `conditioning_3:CONDITIONING`（4 次）
- `inputcount:INT`（1 次）
- `operation:COMBO`（1 次）
- `conditioning_4:CONDITIONING`（1 次）

## 输出

- `combined:CONDITIONING`（4 次）
- `inputcount:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, null]`（1 次）
- `[4, "combine", null]`（1 次）
- `[3, "combine", null]`（1 次）
- `[3, "concat", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
