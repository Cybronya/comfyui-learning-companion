# FlashVSRNode

## 节点类型

`FlashVSRNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（1 次）
- `mode:COMBO`（1 次）
- `scale:INT`（1 次）
- `color_fix:BOOLEAN`（1 次）
- `tiled_vae:BOOLEAN`（1 次）
- `tiled_dit:BOOLEAN`（1 次）
- `tile_size:INT`（1 次）
- `tile_overlap:INT`（1 次）
- `unload_dit:BOOLEAN`（1 次）
- `sparse_ratio:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["tiny", 2, true, true, true, 256, 24, true, 2, 3, 11, 981748245779258, "randomize", "cuda", "bf16", "sparse_sage_attent`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
