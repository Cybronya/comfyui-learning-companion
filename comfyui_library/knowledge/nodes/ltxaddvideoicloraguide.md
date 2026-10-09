# LTXAddVideoICLoRAGuide

## 节点类型

`LTXAddVideoICLoRAGuide`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `latent:LATENT`（1 次）
- `image:IMAGE`（1 次）
- `frame_idx:INT`（1 次）
- `strength:FLOAT`（1 次）
- `latent_downscale_factor:FLOAT`（1 次）
- `crop:COMBO`（1 次）
- `use_tiled_encode:BOOLEAN`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, 1, "center", false, 256, 64]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
