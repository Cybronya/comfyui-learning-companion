# BatchCropFromMask

## 节点类型

`BatchCropFromMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `original_images:IMAGE`（2 次）
- `masks:MASK`（2 次）
- `crop_size_mult:FLOAT`（2 次）
- `bbox_smooth_alpha:FLOAT`（2 次）

## 输出

- `original_images:IMAGE`（2 次）
- `cropped_images:IMAGE`（2 次）
- `bboxes:BBOX`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
