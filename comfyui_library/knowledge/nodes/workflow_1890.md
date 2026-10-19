# workflow>工作组（勿动）

## 节点类型

`workflow>工作组（勿动）`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `条件:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `Latent:LATENT`（1 次）
- `模型:MODEL`（1 次）
- `条件:CONDITIONING`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["z_image_turbo_bf16.safetensors", "default", "qwen_3_4b.safetensors", "lumina2", "default", "ae.safetensors", 1024, 102`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
