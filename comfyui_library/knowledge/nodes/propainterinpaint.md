# ProPainterInpaint

## 节点类型

`ProPainterInpaint`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `mask_dilates:INT`（1 次）
- `flow_mask_dilates:INT`（1 次）
- `ref_stride:INT`（1 次）
- `neighbor_length:INT`（1 次）
- `subvideo_length:INT`（1 次）
- `raft_iter:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `FLOW_MASK:MASK`（1 次）
- `MASK_DILATE:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[640, 360, 0, 0, 4, 24, 200, 30, "disable"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
