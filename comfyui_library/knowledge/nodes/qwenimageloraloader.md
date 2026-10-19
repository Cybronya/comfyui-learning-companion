# QwenImageLoraLoader

## 节点类型

`QwenImageLoraLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）
- `strength_clip:FLOAT`（1 次）
- `lora_alpha:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen _ 极致真实写实人像摄影_v1.0.safetensors", 0.8, 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
