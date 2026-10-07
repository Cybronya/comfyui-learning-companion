# ByteDanceSeedreamLayerSeparationNodeV2

## 节点类型

`ByteDanceSeedreamLayerSeparationNodeV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model.image:IMAGE`（1 次）

## 输出

- `base_image:IMAGE`（1 次）
- `base_mask:MASK`（1 次）
- `layers:IMAGE`（1 次）
- `masks:MASK`（1 次）
- `bboxes:BOUNDING_BOX`（1 次）
- `layer_stack:LAYERS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedream 5.0 flash", "Separate the image into three layers: the main character and the ship; the background; text, ico`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
