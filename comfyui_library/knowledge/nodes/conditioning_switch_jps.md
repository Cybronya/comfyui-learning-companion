# Conditioning Switch (JPS)

## 节点类型

`Conditioning Switch (JPS)`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `con_1:CONDITIONING`（3 次）
- `con_2:CONDITIONING`（3 次）
- `con_3:CONDITIONING`（3 次）
- `con_4:CONDITIONING`（3 次）
- `con_5:CONDITIONING`（3 次）
- `select:INT`（3 次）

## 输出

- `con_out:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
