# ImageUpscaleWithModelCUDAspeedFixed

## 节点类型

`ImageUpscaleWithModelCUDAspeedFixed`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `upscale_model:UPSCALE_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `use_autocast:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `tile_size:INT`（1 次）
- `overlap:INT`（1 次）
- `enable_compile:COMBO`（1 次）
- `optimization_level:COMBO`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", "fp16", 1024, 8, "enable", "speed", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
