# FlashVSRNodeAdv

## 节点类型

`FlashVSRNodeAdv`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipe:PIPE`（5 次）
- `frames:IMAGE`（5 次）
- `scale:INT`（5 次）
- `color_fix:BOOLEAN`（5 次）
- `tiled_vae:BOOLEAN`（5 次）
- `tiled_dit:BOOLEAN`（5 次）
- `tile_size:INT`（5 次）
- `tile_overlap:INT`（5 次）
- `unload_dit:BOOLEAN`（5 次）
- `sparse_ratio:FLOAT`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, true, true, true, 256, 24, false, 1.8, 2.8000000000000003, 9, 880348186621449, "randomize"]`（3 次）
- `[2, true, true, true, 256, 24, false, 1.8, 2.8000000000000003, 9, 913429076854800, "randomize"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
