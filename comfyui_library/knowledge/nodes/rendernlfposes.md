# RenderNLFPoses

## 节点类型

`RenderNLFPoses`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `nlf_poses:NLFPRED`（1 次）
- `dw_poses:DWPOSES`（1 次）
- `ref_dw_pose:DWPOSES`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `draw_face:BOOLEAN`（1 次）
- `draw_hands:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 896, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
