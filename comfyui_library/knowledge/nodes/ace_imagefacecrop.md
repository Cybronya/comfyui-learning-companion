# ACE_ImageFaceCrop

## 节点类型

`ACE_ImageFaceCrop`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:COMBO`（3 次）
- `crop_width:INT`（3 次）
- `crop_height:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）
- `FACE_DETECTED:BOOLEAN`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["insightface", 1024, 1024]`（2 次）
- `["insightface", 512, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
