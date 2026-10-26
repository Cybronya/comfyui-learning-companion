# MatAnyone

## 节点类型

`MatAnyone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `src_video:IMAGE`（1 次）
- `foreground_mask:IMAGE`（1 次）
- `foreground_MASK:MASK`（1 次）
- `solid_color:IMAGE`（1 次）
- `mask_frame:INT`（1 次）
- `n_warmup:INT`（1 次）
- `max_internal_size:INT`（1 次）
- `max_mem_frames:INT`（1 次）
- `use_long_term:BOOLEAN`（1 次）

## 输出

- `matte:IMAGE`（1 次）
- `green_screen:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 10, -1, 5, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
