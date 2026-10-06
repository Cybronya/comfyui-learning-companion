# ImageConcatenateMulti_UTK

## 节点类型

`ImageConcatenateMulti_UTK`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_1:IMAGE`（2 次）
- `image_2:IMAGE`（2 次）
- `image_3:IMAGE`（2 次）
- `image_4:IMAGE`（2 次）
- `mode:COMBO`（2 次）
- `direction:COMBO`（2 次）
- `match_image_size:BOOLEAN`（2 次）
- `max_size:INT`（2 次）
- `background_color:COMBO`（2 次）
- `gap:INT`（2 次）

## 输出

- `images:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sequential", "right", true, 4096, "gray", 20]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
