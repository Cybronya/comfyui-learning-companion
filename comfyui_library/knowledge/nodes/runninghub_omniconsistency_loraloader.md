# RunningHub OmniConsistency LoraLoader

## 节点类型

`RunningHub OmniConsistency LoraLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `lora_name:COMBO`（2 次）

## 输出

- `style_lora:OCPipeline`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Ghibli_rank128_bf16.safetensors"]`（2 次）
- `["Pixel_rank128_bf16.safetensors"]`（1 次）
- `["Pop_Art_rank128_bf16.safetensors"]`（1 次）
- `[null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
