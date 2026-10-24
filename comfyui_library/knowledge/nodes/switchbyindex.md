# SwitchByIndex

## 节点类型

`SwitchByIndex`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `A:*`（3 次）
- `B:*`（3 次）
- `index:INT`（2 次）
- `flat:COMBO`（2 次）

## 输出

- `list:*`（3 次）
- `count:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "off"]`（2 次）
- `[1, "off"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
