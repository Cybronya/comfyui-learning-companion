# LoraSave

## 节点类型

`LoraSave`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_diff:MODEL`（5 次）
- `text_encoder_diff:CLIP`（5 次）
- `filename_prefix:STRING`（5 次）
- `rank:INT`（5 次）
- `lora_type:COMBO`（5 次）
- `bias_diff:BOOLEAN`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["loras/ComfyUI_extracted_lora", 8, "温婉唐代古典美人.safetensors", true]`（2 次）
- `["loras/ComfyUI_extracted_lora", 8, "暗黑哥特人像.safetensors", true]`（2 次）
- `["loras/ComfyUI_extracted_lora", 8, "standard", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
