# LoraLoaderBlockWeight //Inspire

## 节点类型

`LoraLoaderBlockWeight //Inspire`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）

## 输出

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `populated_vector:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["All", "SDXL-国潮-泼墨_V1_ananmo.safetensors", 1, 1, false, 214617206783613, "fixed", 1, 1, "SDXL-ALL:1,1,1,1,1,1,1,1,1,1,1`（1 次）
- `["All", "网红模特.safetensors", 1, 1, false, 214617206783613, "fixed", 1, 1, "FLUX-ALL:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
