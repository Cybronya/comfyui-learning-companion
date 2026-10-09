# TensorLoopOpen

## 节点类型

`TensorLoopOpen`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `initial_value:IMAGE,MASK,LATENT`（1 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（1 次）
- `mode.iterations:INT`（1 次）

## 输出

- `flow_control:FLOW_CONTROL`（1 次）
- `previous_value:*`（1 次）
- `accumulated_count:INT`（1 次）
- `current_iteration:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["iterations", 10]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
