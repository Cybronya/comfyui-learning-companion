# TextEncodeQwenImageEditPlus_lrzjason

## 节点类型

`TextEncodeQwenImageEditPlus_lrzjason`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `enable_resize:BOOLEAN`（3 次）
- `enable_vl_resize:BOOLEAN`（3 次）

## 输出

- `conditioning:CONDITIONING`（3 次）
- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true, true, "lanczos", "disabled", "<|im_start|>system\nDescribe the key features of the input image (color, shape,`（2 次）
- `["", true, true, false, "lanczos", "disabled", "Describe the key features of the input image (color, shape, size, textur`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
