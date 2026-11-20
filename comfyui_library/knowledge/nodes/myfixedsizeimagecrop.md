# MyFixedSizeImageCrop

## 节点类型

`MyFixedSizeImageCrop`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `size_preset:COMBO`（1 次）
- `resolution_preset:COMBO`（1 次）
- `crop_anchor:COMBO`（1 次）
- `upscale_method:COMBO`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `selected_preset:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4:3", "自动按长边", "居中", "最近邻"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
