# ImagePadForOutpaintTargetSize

## 节点类型

`ImagePadForOutpaintTargetSize`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `feathering:INT`（1 次）
- `upscale_method:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[544, 960, 0, "nearest-exact"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
