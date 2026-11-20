# StartLoop

## 节点类型

`StartLoop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `parent_iteration:INT`（1 次）
- `initial_iteration_value:*`（1 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（1 次）
- `mode.num_iterations:INT`（1 次）
- `cache_iterations:BOOLEAN`（1 次）

## 输出

- `iteration_index:INT`（1 次）
- `is_first:BOOLEAN`（1 次）
- `is_last:BOOLEAN`（1 次）
- `list_item:*`（1 次）
- `current_iteration_value:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["simple", 6, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
