# SubtitleEraserProPainter

## 节点类型

`SubtitleEraserProPainter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `masks:MASK`（3 次）
- `propainter_model:COMBO`（3 次）
- `raft_model:COMBO`（3 次）
- `flow_model:COMBO`（3 次）
- `mask_dilation:INT`（3 次）
- `ref_stride:INT`（3 次）
- `neighbor_length:INT`（3 次）
- `subvideo_length:INT`（3 次）

## 输出

- `erased_images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ProPainter.pth", "raft-things.pth", "recurrent_flow_completion.pth", 4, 10, 10, 80]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
