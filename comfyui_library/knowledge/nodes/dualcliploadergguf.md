# DualCLIPLoaderGGUF

## 节点类型

`DualCLIPLoaderGGUF`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输出

- `CLIP:CLIP`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sd3/t5xxl_fp16.safetensors", "sd3/clip_l.safetensors", "flux"]`（1 次）
- `["sd3/clip_l.safetensors", "sd3/t5xxl_fp8_e4m3fn.safetensors", "flux"]`（1 次）
- `["t5-v1_1-xxl-encoder-Q4_K_S.gguf", "sd3/clip_l.safetensors", "flux"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
