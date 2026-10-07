# AutoCropFaces

## 节点类型

`AutoCropFaces`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `number_of_faces:INT`（1 次）
- `scale_factor:FLOAT`（1 次）
- `shift_factor:FLOAT`（1 次）
- `start_index:INT`（1 次）
- `max_faces_per_image:INT`（1 次）
- `aspect_ratio:COMBO`（1 次）

## 输出

- `face:IMAGE`（1 次）
- `output_1:CROP_DATA`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1.5, 0.49643059000081846, 0, 50, "2:3"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
