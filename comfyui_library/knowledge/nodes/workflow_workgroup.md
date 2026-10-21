# workflow>workgroup

## 节点类型

`workflow>workgroup`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `条件:CONDITIONING`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `vae_name:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `unet_name:COMBO`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1200, 1200, 1, "z_image_turbo-vae.safetensors", "qwen_3_4b.safetensors", "lumina2", "default", "zImageTurboNSFW_80BF16.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
