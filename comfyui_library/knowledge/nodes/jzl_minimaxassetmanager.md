# JZL_MiniMaxAssetManager

## 节点类型

`JZL_MiniMaxAssetManager`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `run_mode:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `duration:INT`（1 次）
- `scale_factor:FLOAT`（1 次）
- `upscale_scale:FLOAT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `音频:AUDIO`（1 次）
- `已处理剧本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["故事拆解模式", "分辨率：544x960丨每段帧数：124丨共计段数：8丨总帧数：992丨总时长：40秒", "9:16 (Portrait Widescreen)", 0.5, 5, 1, 1, 8, "悬疑推理", "dongge`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
