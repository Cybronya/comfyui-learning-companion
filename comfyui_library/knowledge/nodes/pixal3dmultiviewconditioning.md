# Pixal3DMultiViewConditioning

## 节点类型

`Pixal3DMultiViewConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip_vision_model:CLIP_VISION`（1 次）
- `front:IMAGE`（1 次）
- `left:IMAGE`（1 次）
- `back:IMAGE`（1 次）
- `right:IMAGE`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
