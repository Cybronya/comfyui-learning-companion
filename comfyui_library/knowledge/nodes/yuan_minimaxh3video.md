# Yuan_MiniMaxH3Video

## 节点类型

`Yuan_MiniMaxH3Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `ref_images:IMAGE`（2 次）
- `ref_video_1:IMAGE`（2 次）
- `ref_video_audio_1:AUDIO`（2 次）
- `ref_audio_1:AUDIO`（2 次）
- `mode:COMBO`（2 次）
- `prompt:STRING`（2 次）
- `width:INT`（2 次）

## 输出

- `正向:CONDITIONING`（2 次）
- `潜空间:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["参考图生视频", "", 832, 480, 124, "匹配", 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
