# RebelsKrea2OutpaintCanvas

## 节点类型

`RebelsKrea2OutpaintCanvas`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source:IMAGE`（1 次）
- `direction:COMBO`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `source_max_edge:INT`（1 次）
- `seam_px:INT`（1 次）

## 输出

- `condition:IMAGE`（1 次）
- `placed_source:IMAGE`（1 次）
- `placement:STRING`（1 次）
- `canvas_width:INT`（1 次）
- `canvas_height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["extend_width_both", 2048, 1024, 384, 32]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
