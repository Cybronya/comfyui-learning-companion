# workflow>wan2.2

## 节点类型

`workflow>wan2.2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `UNETLoader unet_name:COMBO`（1 次）
- `UNETLoader weight_dtype:COMBO`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）
- `LoraLoaderModelOnly lora_name:COMBO`（1 次）
- `LoraLoaderModelOnly strength_model:FLOAT`（1 次）
- `LoraLoaderModelOnly 2 lora_name:COMBO`（1 次）
- `LoraLoaderModelOnly 2 strength_model:FLOAT`（1 次）

## 输出

- `模型:MODEL`（1 次）
- `ModelSamplingSD3 模型:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors", "fp8_e4m3fn", "wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors", "f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
