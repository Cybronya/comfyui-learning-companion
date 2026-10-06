# workflow/模型组

## 节点类型

`workflow/模型组`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输出

- `VAE:VAE`（4 次）
- `CLIP:CLIP`（4 次）
- `模型:MODEL`（4 次）
- `LoraLoader 模型:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.sft", "sd3/t5xxl_fp16.safetensors", "sd3/clip_l.safetensors", "flux", "default", "flux1-dev-fp8-Kijai.safetensors",`（1 次）
- `["flux1-dev.sft", "fp8_e4m3fn", "sd3/t5xxl_fp16.safetensors", "longclip-L.pt", "flux", "default", "ae.sft", "2.12大胸美女-00`（1 次）
- `["sd3/clip_l.safetensors", "sd3/t5xxl_fp8_e4m3fn.safetensors", "flux", "default", "flux1-dev-fp8-Kijai.safetensors", "fp`（1 次）
- `["ae.sft", "sd3/t5xxl_fp8_e4m3fn.safetensors", "sd3/clip_l.safetensors", "flux", "default", "flux1-dev.sft", "fp8_e4m3fn`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
