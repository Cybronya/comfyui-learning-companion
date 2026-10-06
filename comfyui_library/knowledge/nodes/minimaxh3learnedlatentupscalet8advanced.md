# MiniMaxH3LearnedLatentUpscaleT8Advanced

## 节点类型

`MiniMaxH3LearnedLatentUpscaleT8Advanced`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `av_latent:LATENT`（14 次）
- `model_name:COMBO`（14 次）
- `size_mode:COMBO`（14 次）
- `scale_by:FLOAT`（14 次）
- `target_megapixels:FLOAT`（14 次）
- `target_width:INT`（14 次）
- `target_height:INT`（14 次）
- `aspect_policy:COMBO`（14 次）
- `max_anisotropy:FLOAT`（14 次）
- `precision:COMBO`（14 次）

## 输出

- `av_latent:LATENT`（14 次）
- `width:INT`（14 次）
- `height:INT`（14 次）
- `report_json:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_latent_upscaler_3d_fp16.safetensors", "scale_by", 1.5000000000000002, 1, 1280, 704, "preserve_source", 1.05`（5 次）
- `["h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", "scale_by", 1.5000000000000002, 1, 1280, 704, "preserve_source`（5 次）
- `["minimax_h3_latent_upscaler_3d_fp16_V2.safetensors", "scale_by", 1.5000000000000002, 1, 1280, 704, "preserve_source", 1`（2 次）
- `["h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", "scale_by", 1.2000000000000002, 1, 1280, 704, "preserve_source`（1 次）
- `["h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", "scale_by", 1.2000000000000002, 2.0000000000000004, 1280, 704,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
