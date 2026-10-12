# Depthflow

## 节点类型

`Depthflow`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `depth_map:IMAGE`（4 次）
- `motion:DEPTHFLOW_MOTION`（4 次）
- `effects:DEPTHFLOW_EFFECTS`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 30, 30, 60, 100, 1, 0, "mirror"]`（2 次）
- `[1, 30, 30, 60, 100, 0, 0, "mirror"]`（1 次）
- `[1, 30, 30, 60, 100, 0, 0.2, "mirror"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
