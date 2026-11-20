# H3LongVideo

## 节点类型

`H3LongVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `prompts:H3_PROMPTS`（2 次）
- `ref_images.ref_image_0:IMAGE`（2 次）
- `ref_images.ref_image_1:IMAGE`（2 次）
- `ref_images.ref_image_2:IMAGE`（2 次）
- `ref_images.ref_image_3:IMAGE`（2 次）
- `ref_images.ref_image_4:IMAGE`（2 次）

## 输出

- `合并视频:VIDEO`（2 次）
- `最后一段 latent:LATENT`（2 次）
- `生成信息:STRING`（2 次）
- `LATENT 文件路径:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 10, "16:9 (Widescreen)", 0.2, 1074479698903066, "randomize", 8, "er_sde", "simple", 22, "fixed", 1, "match", false, `（1 次）
- `[3, 10, "16:9 (Widescreen)", 1, 1022746812379149, "randomize", 8, "er_sde", "simple", 22, "fixed", 1, "match", false, "H`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
