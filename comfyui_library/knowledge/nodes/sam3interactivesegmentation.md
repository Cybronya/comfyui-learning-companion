# SAM3InteractiveSegmentation

## 节点类型

`SAM3InteractiveSegmentation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sam3_model:SAM3_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `positive_points:SAM3_POINTS_PROMPT`（1 次）
- `negative_points:SAM3_POINTS_PROMPT`（1 次）
- `box:SAM3_BOXES_PROMPT`（1 次）
- `multimask_output:BOOLEAN`（1 次）

## 输出

- `masks:MASK`（1 次）
- `visualization:IMAGE`（1 次）
- `boxes:STRING`（1 次）
- `scores:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
