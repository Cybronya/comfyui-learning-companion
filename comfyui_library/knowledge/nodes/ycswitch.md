# YCSwitch

## 节点类型

`YCSwitch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input1:*`（1 次）
- `select:INT`（1 次）
- `sel_mode:BOOLEAN`（1 次）
- `input2:STRING`（1 次）
- `input3:STRING`（1 次）

## 输出

- `selected_value:*`（1 次）
- `selected_label:STRING`（1 次）
- `selected_index:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
