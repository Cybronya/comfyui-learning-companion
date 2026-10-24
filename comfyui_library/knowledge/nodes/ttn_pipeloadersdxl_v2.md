# ttN pipeLoaderSDXL_v2

## 节点类型

`ttN pipeLoaderSDXL_v2`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_override:MODEL`（4 次）
- `clip_override:CLIP`（4 次）
- `optional_lora_stack:LORA_STACK`（4 次）
- `optional_controlnet_stack:CONTROL_NET_STACK`（4 次）
- `refiner_model_override:MODEL`（4 次）
- `refiner_clip_override:CLIP`（4 次）
- `prepend_positive_g:STRING`（4 次）
- `prepend_positive_l:STRING`（4 次）
- `prepend_negative_g:STRING`（4 次）
- `prepend_negative_l:STRING`（4 次）

## 输出

- `sdxl_pipe:PIPE_LINE_SDXL`（4 次）
- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `vae:VAE`（4 次）
- `clip:CLIP`（4 次）
- `refiner_model:MODEL`（4 次）
- `refiner_positive:CONDITIONING`（4 次）
- `refiner_negative:CONDITIONING`（4 次）
- `refiner_clip:CLIP`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["AdamMix_SDXL_gufeng丨诗画古风_v1.2.safetensors", "Default", "Baked VAE", -2, "", "None", "Default", "1girl", "", "", "", "1`（1 次）
- `["AdamMix_SDXL_gufeng丨诗画古风_v1.2.safetensors", "Default", "Baked VAE", -2, "", "None", "Default", "1girl, outdoor, high q`（1 次）
- `["AdamMix_SDXL_gufeng丨诗画古风_v1.2.safetensors", "Default", "Baked VAE", -2, "", "None", "Default", "An Asian with artistic`（1 次）
- `["albedobaseXL_v31Large.safetensors", "Default", "Baked VAE", -2, "", "sd_xl_refiner_1.0_0.9vae_1.0.safetensors", "Defau`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
