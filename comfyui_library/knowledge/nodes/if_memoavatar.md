# IF_MemoAvatar

## 节点类型

`IF_MemoAvatar`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `reference_net:MODEL`（1 次）
- `diffusion_net:MODEL`（1 次）
- `vae:VAE`（1 次）
- `image_proj:IMAGE_PROJ`（1 次）
- `audio_proj:AUDIO_PROJ`（1 次）
- `emotion_classifier:EMOTION_CLASSIFIER`（1 次）

## 输出

- `video_path:STRING`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 16, 30, 20, 3.5, 537, "fixed", "memo_video", {"serialize": false, "size": [256, 256]}]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
