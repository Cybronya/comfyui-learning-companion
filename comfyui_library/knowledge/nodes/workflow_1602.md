# workflow>换脸

## 节点类型

`workflow>换脸`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `image_from:IMAGE`（1 次）
- `image_to:IMAGE`（1 次）
- `Image Paste Crop image:IMAGE`（1 次）
- `library:COMBO`（1 次）
- `provider:COMBO`（1 次）
- `number_of_faces:INT`（1 次）
- `scale_factor:FLOAT`（1 次）
- `shift_factor:FLOAT`（1 次）
- `start_index:INT`（1 次）

## 输出

- `face:IMAGE`（1 次）
- `IMAGE:IMAGE`（1 次）
- `AutoCropFaces face:IMAGE`（1 次）
- `CROP_DATA:CROP_DATA`（1 次）
- `Image Paste Crop IMAGE:IMAGE`（1 次）
- `MASK:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["insightface", "CPU", 1, 5, 0.45, 0, 50, "1:1", 1, 5, 0.45, 0, 50, "1:1", 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
