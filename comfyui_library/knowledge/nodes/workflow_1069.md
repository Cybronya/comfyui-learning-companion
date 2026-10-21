# workflow>克莱因高清

## 节点类型

`workflow>克莱因高清`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `clip_name:COMBO`（3 次）
- `type:COMBO`（3 次）
- `device:COMBO`（3 次）
- `vae_name:COMBO`（3 次）
- `unet_name:COMBO`（3 次）
- `weight_dtype:COMBO`（3 次）
- `CLIPLoader clip_name:COMBO`（3 次）
- `CLIPLoader type:COMBO`（3 次）

## 输出

- `show_help:STRING`（3 次）
- `遮罩:MASK`（3 次）
- `原始大小:BOX`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `batch_size:INT`（3 次）
- `output:*`（3 次）
- `图像:IMAGE`（3 次）
- `easy cleanGpuUsed output:*`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_3_4b.safetensors", "lumina2", "default", "z_image_turbo-vae.safetensors", "z_image_turbo_bf16.safetensors", "defa`（1 次）
- `["qwen_3_4b.safetensors", "lumina2", "default", "z_image_turbo-vae.safetensors", "z_image_turbo_bf16.safetensors", "defa`（1 次）
- `["qwen_3_4b.safetensors", "lumina2", "default", "z_image_turbo-vae.safetensors", "z_image_turbo_bf16.safetensors", "defa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
