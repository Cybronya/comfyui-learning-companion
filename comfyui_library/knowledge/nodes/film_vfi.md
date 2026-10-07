# FILM VFI

## 节点类型

`FILM VFI`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `frames:IMAGE`（2 次）
- `optional_interpolation_states:INTERPOLATION_STATES`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["film_net_fp32.pt", 10, 2]`（1 次）
- `["film_net_fp32.pt", 10, 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
