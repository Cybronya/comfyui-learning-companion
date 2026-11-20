# ViggleRemakeConditioningByShenGun

## 节点类型

`ViggleRemakeConditioningByShenGun`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `vae:VAE`（4 次）
- `audio_vae:VAE`（4 次）
- `source:IMAGE`（4 次）
- `ref_1:IMAGE`（4 次）
- `audio:AUDIO`（4 次）
- `ref_2:IMAGE`（4 次）
- `ref_3:IMAGE`（4 次）
- `ref_4:IMAGE`（4 次）
- `prompt:STRING`（4 次）

## 输出

- `positive:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subject_definitions:\n<Video 1> is the source video for the editing task: one continuous handheld vertical take in a b`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
