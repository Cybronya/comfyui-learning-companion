# LTXVImgToVideoInplaceKJ

## 节点类型

`LTXVImgToVideoInplaceKJ`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `vae:VAE`（5 次）
- `latent:LATENT`（5 次）
- `image_1:IMAGE`（5 次）
- `image_2:IMAGE`（5 次）
- `image_3:IMAGE`（5 次）
- `image_4:IMAGE`（5 次）
- `image_5:IMAGE`（5 次）
- `index_1:INT`（5 次）
- `strength_1:FLOAT`（5 次）
- `index_2:INT`（5 次）

## 输出

- `latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1", 1, 0, 1, 0, 1, 0, 1, 0, 1]`（4 次）
- `["3", 1, 1, 1, 121, 1, 241, 1, 361, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
