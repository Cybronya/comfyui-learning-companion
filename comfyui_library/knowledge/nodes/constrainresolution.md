# ConstrainResolution

## 节点类型

`ConstrainResolution`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `min_res:INT`（2 次）
- `max_res:INT`（2 次）
- `multiple_of:INT`（2 次）
- `resize_method:COMBO`（2 次）
- `constraint_mode:COMBO`（2 次）
- `crop_as_required:BOOLEAN`（2 次）
- `crop_position:COMBO`（2 次）

## 输出

- `resized_image:IMAGE`（2 次）
- `original_image:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `final_aspect_ratio:FLOAT`（2 次）
- `original_aspect_ratio:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[704, 1280, 2, "lanczos", "Prioritize Min Resolution", true, "center"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
