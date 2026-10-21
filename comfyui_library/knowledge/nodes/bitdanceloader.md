# BitDanceLoader

## 节点类型

`BitDanceLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `model_name:COMBO`（15 次）
- `text_encoder_name:COMBO`（15 次）
- `vae_name:COMBO`（15 次）
- `quantization:COMBO`（15 次）
- `load_device:COMBO`（15 次）
- `text_encoder_load_device:COMBO`（15 次）
- `vae_load_device:COMBO`（15 次）
- `attention_mode:COMBO`（15 次）
- `rms_norm_function:COMBO`（15 次）
- `precision:COMBO`（15 次）

## 输出

- `bitdance_model:BITDANCE_MODEL`（15 次）
- `bitdance_text_encoder:BITDANCE_TEXT_ENCODER`（15 次）
- `bitdance_vae:BITDANCE_VAE`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["BitDance_14B_MainModel_FP8.safetensors", "BitDance_TextEncoder_FP8.safetensors", "BitDance_VAE_FP16.safetensors", "fp8`（9 次）
- `["BitDance_14B_MainModel_FP8.safetensors", "BitDance_TextEncoder_FP8.safetensors", "BitDance_VAE_FP16.safetensors", "fp8`（4 次）
- `["BitDance_14B_MainModel_FP8.safetensors", "BitDance_TextEncoder_FP8.safetensors", "BitDance_VAE_FP16.safetensors", "fp8`（1 次）
- `["BitDance_14B_MainModel_FP8.safetensors", "BitDance_TextEncoder_FP8.safetensors", "BitDance_VAE_FP16.safetensors", "fp8`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
