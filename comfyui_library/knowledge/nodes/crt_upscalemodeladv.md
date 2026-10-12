# CRT_UpscaleModelAdv

## 节点类型

`CRT_UpscaleModelAdv`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `upscale_model_name:COMBO`（1 次）
- `use_fixed_resolution:BOOLEAN`（1 次）
- `output_multiplier:FLOAT`（1 次）
- `fixed_width:INT`（1 次）
- `fixed_height:INT`（1 次）
- `tile_count:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `batch_size:INT`（1 次）
- `offload_model:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2xNomosUni_compact_multijpg.pth", false, 1, 1624, 2528, "1", "auto", 1, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
