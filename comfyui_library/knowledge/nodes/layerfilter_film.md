# LayerFilter: Film

## 节点类型

`LayerFilter: Film`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `depth_map:IMAGE`（2 次）
- `center_x:FLOAT`（1 次）
- `center_y:FLOAT`（1 次）
- `saturation:FLOAT`（1 次）
- `vignette_intensity:FLOAT`（1 次）
- `grain_power:FLOAT`（1 次）
- `grain_scale:FLOAT`（1 次）
- `grain_sat:FLOAT`（1 次）
- `grain_shadows:FLOAT`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 0.5, 1, 0.16, 0.2, 1, 0.2, 0.6, 0.2, 30, 2.2, 0.9]`（1 次）
- `[0.5, 0.5, 1, 0.5, 0.10000000000000002, 1, 0.5, 0.5000000000000001, 0.2, 90, 2.2, 0.9]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
