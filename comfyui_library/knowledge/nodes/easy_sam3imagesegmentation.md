# easy sam3ImageSegmentation

## 节点类型

`easy sam3ImageSegmentation`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sam3_model:*`（2 次）
- `images:IMAGE`（2 次）
- `coordinates_positive:STRING`（2 次）
- `coordinates_negative:STRING`（2 次）
- `bboxes:BBOX`（2 次）
- `mask:MASK`（2 次）
- `prompt:STRING`（2 次）
- `threshold:FLOAT`（2 次）
- `keep_model_loaded:BOOLEAN`（2 次）
- `add_background:COMBO`（2 次）

## 输出

- `masks:MASK`（2 次）
- `images:IMAGE`（2 次）
- `obj_masks:MASK`（2 次）
- `boxes:BBOX`（2 次）
- `scores:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Cat ears, ears, ", 0.3, false, "none", -1]`（1 次）
- `["Clothes, stockings, accessories, skirt, skirt hem, underwear, bra, panties, thighhighs, gloves, black gloves, blue ski`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
