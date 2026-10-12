# workflow>Wan2.1模型加载器

## 节点类型

`workflow>Wan2.1模型加载器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `extra_model:VACEPATH`（2 次）
- `multitalk_model:MULTITALKMODEL`（2 次）
- `quantization:COMBO`（2 次）
- `load_device:COMBO`（2 次）
- `attention_mode:COMBO`（2 次）
- `rms_norm_function:COMBO`（2 次）
- `model:COMBO`（2 次）
- `base_precision:COMBO`（2 次）
- `clip_name:COMBO`（2 次）
- `precision:COMBO`（2 次）

## 输出

- `clip:WANTEXTENCODER`（2 次）
- `vae:WANVAE`（2 次）
- `model:WANVIDEOMODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fp8_e4m3fn_scaled", "offload_device", "sageattn", "default", "SCAIL/Wan21-14B-SCAIL-preview_comfy_bf16.safetensors", "`（1 次）
- `["fp8_e4m3fn_scaled", "offload_device", "sageattn", "default", "SCAIL/Wan21-14B-SCAIL-preview_fp8_e4m3fn_scaled_KJ.safet`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
