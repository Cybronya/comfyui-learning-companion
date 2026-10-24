# BatchCLIPSeg

## 节点类型

`BatchCLIPSeg`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `opt_model:CLIPSEGMODEL`（1 次）
- `prev_mask:MASK`（1 次）
- `text:STRING`（1 次）
- `threshold:FLOAT`（1 次）
- `binary_mask:BOOLEAN`（1 次）
- `combine_mask:BOOLEAN`（1 次）
- `use_cuda:BOOLEAN`（1 次）
- `blur_sigma:FLOAT`（1 次）
- `image_bg_level:FLOAT`（1 次）

## 输出

- `Mask:MASK`（1 次）
- `Image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hair", 0.5, true, false, true, 0, 0.5, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
