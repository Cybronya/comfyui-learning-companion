# workflow>Video S2V Extend1

## 节点类型

`workflow>Video S2V Extend1`

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
- `video_latent:LATENT`（1 次）
- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（1 次）
- `ref_image:IMAGE`（1 次）
- `control_video:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `samples1:LATENT`（1 次）
- `length:INT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 0, "fixed", 4, 1, "uni_pc", "simple", 1, "t"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
