# FeiHouEasyH3RHLoader

## 节点类型

`FeiHouEasyH3RHLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `lora_stack:FEIHOU_MERGE_LORA_STACK`（3 次）
- `fl2va_model:COMBO`（3 次）
- `ref2va_model:COMBO`（3 次）
- `text_encoder:COMBO`（3 次）
- `video_vae:COMBO`（3 次）
- `audio_vae:COMBO`（3 次）
- `custom_second_sampling_models:BOOLEAN`（3 次）
- `second_fl2va_model:COMBO`（3 次）
- `second_ref2va_model:COMBO`（3 次）
- `second_sampling_use_lora:BOOLEAN`（3 次）

## 输出

- `h3_bundle:MINIMAX_H3_BUNDLE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors", "minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors", "qw`（2 次）
- `["minimax_h3_hybrid_fl2va_ref2va_zs05_b25-49_int8.safetensors", "minimax_h3_hybrid_fl2va_ref2va_zs05_b25-49_int8.safeten`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
