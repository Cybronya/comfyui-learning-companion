# Yuan_H3Upscale3D

## 节点类型

`Yuan_H3Upscale3D`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `latent:LATENT`（1 次）
- `model_name:STRING`（1 次）
- `resize_type:COMBO`（1 次）
- `scale:FLOAT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `潜空间:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_latent_upscaler_3d_fp16.safetensors", "按倍数缩放", 1.5, 1920, 1080]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
