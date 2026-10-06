# LoraLoader

## 节点类型

`LoraLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 22 个 workflow 中。

## 输入

- `model:MODEL`（25 次）
- `clip:CLIP`（25 次）
- `lora_name:COMBO`（25 次）
- `strength_model:FLOAT`（25 次）
- `strength_clip:FLOAT`（25 次）

## 输出

- `MODEL:MODEL`（25 次）
- `CLIP:CLIP`（25 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDXL\\add_details_xl.safetensors", 0.8, 1]`（3 次）
- `["奈良手菊.safetensors", 0.7, 0.7]`（3 次）
- `["DX888HinataV3.safetensors", 0.4, 0.4]`（3 次）
- `["Boruto_Uzumaki_-_Next_Generations_-_Illustrious_Commission.safetensors", 0.6, 0.6]`（3 次）
- `["DX888HinataV3.safetensors", 0.6, 0.6]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
