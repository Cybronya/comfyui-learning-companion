# SAM3_Detect

## 节点类型

`SAM3_Detect`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `image:IMAGE`（5 次）
- `conditioning:CONDITIONING`（5 次）
- `bboxes:BOUNDING_BOX`（5 次）
- `positive_coords:STRING`（5 次）
- `negative_coords:STRING`（5 次）
- `threshold:FLOAT`（5 次）
- `refine_iterations:INT`（5 次）
- `individual_masks:BOOLEAN`（5 次）

## 输出

- `masks:MASK`（5 次）
- `bboxes:BOUNDING_BOX`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 2, false]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
