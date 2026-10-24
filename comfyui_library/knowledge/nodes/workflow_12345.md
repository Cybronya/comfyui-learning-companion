# workflow>12345

## 节点类型

`workflow>12345`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image1:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image2:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image3:IMAGE`（1 次）
- `Latent:LATENT`（1 次）
- `ckpt_name:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `TextEncodeQwenImageEditPlus prompt:STRING`（1 次）

## 输出

- `模型:MODEL`（1 次）
- `VAE:VAE`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `TextEncodeQwenImageEditPlus CONDITIONING:CONDITIONING`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen-Rapid-AIO-SFW-v10.safetensors", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
