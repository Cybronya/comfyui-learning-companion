# PixaromaLoraLoader

## 节点类型

`PixaromaLoraLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `lora_name:COMBO`（2 次）

## 输出

- `MODEL:MODEL`（2 次）
- `CLIP:CLIP`（2 次）
- `triggers:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["krea2-时尚模特.safetensors", {"defStrength": 1, "civitai": true, "loras": [{"sc": 0.7, "custom": [], "name": "krea2_服装模特.s`（1 次）
- `["guweiz.safetensors", {"defStrength": 1, "civitai": true, "loras": [{"sc": 0.7, "custom": [], "name": "加细节_Krea2_v1.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
