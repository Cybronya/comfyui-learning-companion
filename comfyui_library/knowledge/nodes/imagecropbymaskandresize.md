# ImageCropByMaskAndResize

## 节点类型

`ImageCropByMaskAndResize`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `base_resolution:INT`（1 次）
- `padding:INT`（1 次）
- `min_crop_resolution:INT`（1 次）
- `max_crop_resolution:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `masks:MASK`（1 次）
- `bbox:BBOX`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 0, 128, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
