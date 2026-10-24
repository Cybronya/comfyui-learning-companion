# Personalize_Anything_Sampler

## 节点类型

`Personalize_Anything_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL_PERSONALIZE_ANYTHING`（1 次）
- `iamge:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `bg_image:IMAGE`（1 次）
- `clip:CLIP`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["an anime boy,", "waving his right hand,positioned on the left side of the frame, with an empty oad on the right.", 118`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
