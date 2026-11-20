# workflow>loras

## 节点类型

`workflow>loras`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）
- `LoraLoaderModelOnly lora_name:COMBO`（1 次）
- `LoraLoaderModelOnly strength_model:FLOAT`（1 次）
- `LoraLoaderModelOnly 2 lora_name:COMBO`（1 次）
- `LoraLoaderModelOnly 2 strength_model:FLOAT`（1 次）

## 输出

- `模型:MODEL`（1 次）
- `LoraLoaderModelOnly 模型:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan22_PusaV1_lora_LOW_resized_dynamic_avg_rank_98_bf16.safetensors", 0.5000000000000001, "Wan2.2-Lightning_T2V-v1.1-A1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
