# MiniMaxH3ImageConditioning

## 节点类型

`MiniMaxH3ImageConditioning`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 28 个 workflow 中。

## 输入

- `clip:CLIP`（28 次）
- `vae:VAE`（28 次）
- `images.image_0:IMAGE`（28 次）
- `prompt:STRING`（28 次）
- `width:INT`（28 次）
- `height:INT`（28 次）
- `images.image_1:IMAGE`（21 次）
- `images.image_2:IMAGE`（3 次）
- `images.image_3:IMAGE`（3 次）
- `images.image_4:IMAGE`（3 次）

## 输出

- `positive:CONDITIONING`（28 次）
- `LATENT:LATENT`（28 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 3104, 3104]`（20 次）
- `["", 0, 0]`（3 次）
- `["", 6272, 2688]`（2 次）
- `["A vertical Chinese poster. Background: {在此写画面}. Typography burned into the image: main title『{主标题}』, subtitle『{副标题}』, `（1 次）
- `["A photorealistic image: {在此写场景}. Shot like a real camera, natural light, visible surface texture, no illustration, no `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
