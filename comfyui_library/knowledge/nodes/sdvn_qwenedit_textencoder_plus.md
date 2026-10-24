# SDVN QwenEdit TextEncoder Plus

## 节点类型

`SDVN QwenEdit TextEncoder Plus`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（5 次）
- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `vae:VAE`（5 次）
- `prompt:STRING`（5 次）
- `img_size:INT`（5 次）
- `translate:COMBO`（5 次）
- `seed:INT`（5 次）

## 输出

- `conditioning:CONDITIONING`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, "chinese (simplified)", 1095240565601220, "randomize"]`（1 次）
- `["", 0, "chinese (simplified)", 889059293964079, "randomize"]`（1 次）
- `["", 0, "chinese (simplified)", 938344500138844, "randomize"]`（1 次）
- `["将图1女性的脸换成图2中的女性的脸，细节保持不变\n", 0, "None", 678363377519855, "randomize"]`（1 次）
- `["", 0, "chinese (simplified)", 553779640635398, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
