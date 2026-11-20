# AILab_SDMatte

## 节点类型

`AILab_SDMatte`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `model:COMBO`（1 次）
- `device:COMBO`（1 次）
- `process_res:INT`（1 次）
- `transparent_object:BOOLEAN`（1 次）
- `mask_refine:BOOLEAN`（1 次）
- `sensitivity:FLOAT`（1 次）
- `mask_blur:INT`（1 次）
- `mask_offset:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `MASK_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDMatte", "GPU", 1024, true, false, 0.9, 0, 0, false, "Alpha", "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
