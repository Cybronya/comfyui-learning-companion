# Lora Loader Stack (rgthree)

## 节点类型

`Lora Loader Stack (rgthree)`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model:MODEL`（8 次）
- `clip:CLIP`（8 次）
- `lora_01:COMBO`（8 次）
- `strength_01:FLOAT`（8 次）
- `lora_02:COMBO`（8 次）
- `strength_02:FLOAT`（8 次）
- `lora_03:COMBO`（8 次）
- `strength_03:FLOAT`（8 次）
- `lora_04:COMBO`（8 次）
- `strength_04:FLOAT`（8 次）

## 输出

- `MODEL:MODEL`（8 次）
- `CLIP:CLIP`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen2.1-msj_c1-st7000.safetensors", 0.5000000000000001, "qwen21_detail_slider_v2.safetensors", 1.0000000000000002, "No`（3 次）
- `["Qwen2.1-xm923_c1-st10000.safetensors", 1.0000000000000002, "qwen21_detail_slider_v2.safetensors", 1.0000000000000002, `（2 次）
- `["qwen-image2.1-XM_c1-st8000.safetensors", 0.8800000000000001, "qwen21_detail_slider_v2.safetensors", 1.0000000000000002`（2 次）
- `["qwen-image2.1-mxlz_c1-st6000.safetensors", 0.8800000000000001, "qwen21_detail_slider_v2.safetensors", 1.00000000000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
