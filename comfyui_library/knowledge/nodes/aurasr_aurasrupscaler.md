# AuraSR.AuraSRUpscaler

## 节点类型

`AuraSR.AuraSRUpscaler`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `transparency_mask:MASK`（2 次）
- `model_name:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `reapply_transparency:BOOLEAN`（1 次）
- `tile_batch_size:INT`（1 次）
- `device:COMBO`（1 次）
- `offload_to_cpu:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["model.ckpt", "4x", true, 8, "default", false]`（1 次）
- `["model.safetensors", "4x_overlapped_constant", true, 32, "default", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
