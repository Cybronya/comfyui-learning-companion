# Divide and Conquer Algorithm

## 节点类型

`Divide and Conquer Algorithm`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `upscale_model:UPSCALE_MODEL`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）
- `min_overlap:COMBO`（1 次）
- `min_scale_factor:FLOAT`（1 次）
- `tile_order:COMBO`（1 次）
- `scaling_method:COMBO`（1 次）
- `use_upscale_with_model:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `dac_data:DAC_DATA`（1 次）
- `ui:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1440, 1440, "1/4 Tile", 2, "spiral", "lanczos", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
