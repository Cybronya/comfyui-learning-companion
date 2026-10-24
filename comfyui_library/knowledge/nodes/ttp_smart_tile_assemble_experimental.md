# TTP_Smart_Tile_Assemble_Experimental

## 节点类型

`TTP_Smart_Tile_Assemble_Experimental`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sampled_tiles:IMAGE`（1 次）
- `tile_meta:TTP_SMART_TILE_META`（1 次）
- `tile_set:TTP_SMART_TILE_SET`（1 次）
- `base_image:IMAGE`（1 次）
- `source_image:IMAGE`（1 次）
- `color_reference_image:IMAGE`（1 次）
- `done:BOOLEAN`（1 次）
- `blend_multiplier:FLOAT`（1 次）
- `output_scale:FLOAT`（1 次）
- `use_priority:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `weight_preview:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0, true, "center_crop", 0, "mkl_lab", 0.35, "mask_feather", "off", 8, "auto", "use_if_higher_resolution", 0.55, 0.95`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
