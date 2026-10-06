# TripleCLIPLoader

## 节点类型

`TripleCLIPLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输出

- `CLIP:CLIP`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sd3/clip_g.safetensors", "sd3/clip_l.safetensors", "sd3/t5xxl_fp8_e4m3fn.safetensors"]`（3 次）
- `["sd3/clip_l.safetensors", "sd3/clip_g.safetensors", "sd3/t5xxl_fp8_e4m3fn.safetensors"]`（3 次）
- `["sd3/clip_l.safetensors", "sd3/clip_g.safetensors", "sd3/t5xxl_fp16.safetensors"]`（1 次）
- `["sd3/t5xxl_fp16.safetensors", "longclip-L.pt", "sd3/clip_g.safetensors"]`（1 次）
- `["sd3/t5xxl_fp16.safetensors", "ViT-L-14-TEXT-detail-improved-hiT-GmP-HF.safetensors", "sd3/clip_g.safetensors"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
