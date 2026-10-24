# NunchakuQwenImageLoraStackV2

## 节点类型

`NunchakuQwenImageLoraStackV2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `lora_count:INT`（3 次）
- `cpu_offload:COMBO`（3 次）
- `lora_name_1:COMBO`（3 次）
- `lora_strength_1:FLOAT`（3 次）
- `lora_name_2:COMBO`（3 次）
- `lora_strength_2:FLOAT`（3 次）
- `lora_strength_3:FLOAT`（3 次）
- `lora_strength_4:FLOAT`（3 次）
- `lora_strength_5:FLOAT`（3 次）

## 输出

- `MODEL:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["3", 3, "disable", "多角度.safetensors", 1, "__Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16__Edit8步bf16 r2.0.safetensor`（1 次）
- `["2", 2, "auto", "20251212-80037438.safetensors", 1.0000000000000002, "奇幻国风插画.safetensors", 1.0000000000000002]`（1 次）
- `["2", 2, 2, "disable", "Wuli-Qwen-Image-2512-Turbo-LoRA-4steps-V2.0-bf16(1).safetensors", 0.45000000000000007, "Kook_Qwe`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
