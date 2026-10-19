# Model Switch (JPS)

## 节点类型

`Model Switch (JPS)`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_1:MODEL`（2 次）
- `model_2:MODEL`（2 次）
- `model_3:MODEL`（2 次）
- `model_4:MODEL`（2 次）
- `model_5:MODEL`（2 次）
- `select:INT`（2 次）

## 输出

- `model_out:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
