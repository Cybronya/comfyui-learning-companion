# RemakeConditioning

## 节点类型

`RemakeConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `vae:VAE`（6 次）
- `audio_vae:VAE`（6 次）
- `source:IMAGE`（6 次）
- `ref_1:IMAGE`（6 次）
- `audio:AUDIO`（6 次）
- `ref_2:IMAGE`（6 次）
- `ref_3:IMAGE`（6 次）
- `ref_4:IMAGE`（6 次）
- `prompt:STRING`（6 次）

## 输出

- `positive:CONDITIONING`（6 次）
- `latent:LATENT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subject_definitions:\n<Video 1> is the source video for the editing task: one continuous 9.4 s handheld take on a sunn`（2 次）
- `["", "", 243, 672]`（1 次）
- `["subject_definitions:\n<Video 1> is the source video for the editing task: one continuous 9.4 s handheld take on a sunn`（1 次）
- `["", "", 124, 736]`（1 次）
- `["subject_definitions:\n<Video 1> is the source video for the target video edit.\n<Picture 1> is a frame of the target v`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
