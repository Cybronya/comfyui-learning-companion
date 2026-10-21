# workflow>工作区

## 节点类型

`workflow>工作区`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `positive:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["z_image_turbo_bf16.safetensors", "default", "qwen_3_4b.safetensors", "qwen_image", "default", "ae.safetensors", 366155`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
