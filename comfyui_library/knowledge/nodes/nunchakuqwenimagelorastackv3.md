# NunchakuQwenImageLoraStackV3

## 节点类型

`NunchakuQwenImageLoraStackV3`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `lora_count:INT`（2 次）
- `cpu_offload:COMBO`（2 次）
- `toggle_all:BOOLEAN`（2 次）
- `enabled_1:BOOLEAN`（2 次）
- `lora_name_1:COMBO`（2 次）
- `lora_strength_1:FLOAT`（2 次）
- `lora_name_2:COMBO`（2 次）
- `enabled_3:BOOLEAN`（2 次）
- `lora_strength_3:FLOAT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1", 1, true, "auto", true, "Qwen-Image-2512-Lightning-4steps-V1.0-bf16.safetensors", 1]`（1 次）
- `["1", 1, true, "disable", true, "Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
