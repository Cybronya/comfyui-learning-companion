# NunchakuZImageTurboLoraStackV4

## 节点类型

`NunchakuZImageTurboLoraStackV4`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `lora_count:INT`（1 次）
- `toggle_all:BOOLEAN`（1 次）
- `enabled_1:BOOLEAN`（1 次）
- `lora_name_1:COMBO`（1 次）
- `lora_strength_1:FLOAT`（1 次）
- `enabled_2:BOOLEAN`（1 次）
- `lora_name_2:COMBO`（1 次）
- `lora_strength_2:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2", 2, true, true, "Qwen 2511-Unblur-Anything V2.0.safetensors", 0.5000000000000001, true, "Kook_Zimage_真实幻想_Turbo.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
