# QwenImageIntegratedKSampler

## 节点类型

`QwenImageIntegratedKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `image5:IMAGE`（2 次）
- `latent:LATENT`（2 次）
- `controlnet_data:CONTROL_NET_DATA`（2 次）

## 输出

- `生成图像Image:IMAGE`（2 次）
- `（可选）Latent:LATENT`（2 次）
- `缩放后原图Scaled Image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["溶图,纠正产品透视角度和光影并使产品融入背景", "", "图生图 image-to-image", 1, 0, 0, 285514781737175, "randomize", 8, 1, "euler", "simple", 1, `（1 次）
- `["溶图,纠正产品透视角度和光影并使产品融入背景", "", "图生图 image-to-image", 1, 0, 0, 504956230618996, "randomize", 8, 1, "euler", "simple", 1, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
