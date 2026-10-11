# Image_Upscaletile

## 节点类型

`Image_Upscaletile`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model_name:COMBO`（2 次）
- `upscale_by:FLOAT`（2 次）
- `tile_size:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1x-ITF-SkinDiffDetail-Lite-v1.pth", 2, 512]`（1 次）
- `["2xNomosUni_span_multijpg_ldl.pth", 1.5, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
