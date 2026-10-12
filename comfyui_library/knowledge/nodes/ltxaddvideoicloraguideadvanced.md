# LTXAddVideoICLoRAGuideAdvanced

## 节点类型

`LTXAddVideoICLoRAGuideAdvanced`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `positive:CONDITIONING`（9 次）
- `negative:CONDITIONING`（9 次）
- `vae:VAE`（9 次）
- `latent:LATENT`（9 次）
- `image:IMAGE`（9 次）
- `attention_mask:MASK`（9 次）
- `frame_idx:INT`（9 次）
- `strength:FLOAT`（9 次）
- `latent_downscale_factor:FLOAT`（9 次）
- `crop:COMBO`（9 次）

## 输出

- `positive:CONDITIONING`（9 次）
- `negative:CONDITIONING`（9 次）
- `latent:LATENT`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0.7, 1, "disabled", false, 256, 64, 1]`（5 次）
- `[0, 1, 1, "disabled", false, 256, 64, 1]`（2 次）
- `[0, 0.7000000000000002, 1, "disabled", false, 256, 64, 1]`（1 次）
- `[0, 0.7, 1, "center", false, 256, 64, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
