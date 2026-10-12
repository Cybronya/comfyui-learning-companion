# HDR360Generate

## 节点类型

`HDR360Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_image:IMAGE`（1 次）
- `projection_type:COMBO`（1 次）
- `output_width:INT`（1 次）
- `output_height:INT`（1 次）
- `horizontal_fov:FLOAT`（1 次）
- `vertical_fov:FLOAT`（1 次）
- `rotation_x:FLOAT`（1 次）
- `rotation_y:FLOAT`（1 次）
- `rotation_z:FLOAT`（1 次）
- `interpolation:COMBO`（1 次）

## 输出

- `panorama:IMAGE`（1 次）
- `projection_map:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Equirectangular", 4096, 2048, 360, 120, 180, 0, 0, "Bilinear", "Mirror", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
