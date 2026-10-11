# SFH3MultimodalDirector

## 节点类型

`SFH3MultimodalDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `video_vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `storyboard_text:STRING`（2 次）
- `storyboard_images:IMAGE`（2 次）
- `reference_images:IMAGE`（2 次）
- `reference_video_1:IMAGE`（2 次）
- `reference_video_2:IMAGE`（2 次）
- `reference_video_3:IMAGE`（2 次）

## 输出

- `模型:MODEL`（2 次）
- `正向条件:CONDITIONING`（2 次）
- `音视频潜空间:LATENT`（2 次）
- `编译提示词:STRING`（2 次）
- `帧数:INT`（2 次）
- `帧率:FLOAT`（2 次）
- `输出宽度:INT`（2 次）
- `输出高度:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["宫格模式", 12, "16:9 横屏", "匹配输出（推荐）", "{\"version\":1,\"updatedAt\":1786141461731,\"globalPrompt\":\"电影感真人摄影，热带丛林实景，奇幻生物，自`（1 次）
- `["宫格模式", 12, "16:9 横屏", "匹配输出（推荐）", "{\"version\":1,\"updatedAt\":1786089827080,\"globalPrompt\":\"电影感真人摄影，热带丛林实景，奇幻生物，自`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
