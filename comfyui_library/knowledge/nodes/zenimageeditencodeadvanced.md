# ZenImageEditEncodeAdvanced

## 节点类型

`ZenImageEditEncodeAdvanced`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（5 次）
- `images.image_1:IMAGE`（5 次）
- `images.image_2:IMAGE`（5 次）
- `images.image_3:IMAGE`（5 次）
- `images.image_4:IMAGE`（5 次）
- `vae:VAE`（5 次）
- `prompt:STRING`（5 次）
- `negative_prompt:STRING`（5 次）
- `resolution:INT`（5 次）
- `canvas_mode:COMBO`（5 次）

## 输出

- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "artifacts, gpt-image, washed-out colors, low quality, low resolution, AI slop, deviantart, sloppy lines, rough ske`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
