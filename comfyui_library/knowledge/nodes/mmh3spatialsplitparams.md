# MMH3SpatialSplitParams

## 节点类型

`MMH3SpatialSplitParams`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `upscale_width:INT`（1 次）
- `upscale_height:INT`（1 次）
- `tile_size_mode:COMBO`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）
- `grid_rows:INT`（1 次）
- `grid_cols:INT`（1 次）
- `spatial_w_overlap:INT`（1 次）
- `spatial_h_overlap:INT`（1 次）
- `fade_width:INT`（1 次）

## 输出

- `spatial_split_param:H3_SPATIAL_PARAM`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[864, 480, "rows_cols", 128, 32, 2, 4, 32, 32, 32, 32, 256, "earlier", "linear", true, 70000]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
