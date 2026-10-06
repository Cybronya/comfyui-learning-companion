# CLIPLoaderGGUF

## 节点类型

`CLIPLoaderGGUF`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `clip_name:COMBO`（7 次）
- `type:COMBO`（7 次）

## 输出

- `CLIP:CLIP`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3-4b-Z-Image-Engineer-V4-F16.gguf", "lumina2"]`（5 次）
- `["Z-Image-Engineer-V6-Q8_0.gguf", "lumina2"]`（1 次）
- `["qwen_3_4b.safetensors", "qwen_image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
