# TextEncodeQwenImageEditPlusAdv

## 节点类型

`TextEncodeQwenImageEditPlusAdv`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `smart_input:BOOLEAN`（1 次）
- `align_latent:COMBO`（1 次）

## 输出

- `conditioning+:CONDITIONING`（1 次）
- `conditioning-:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["让图1中的女模特右手拿着图2的产品，摆出一个妩媚妖娆的姿势。重新打光。", "", false, "image1_only"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
