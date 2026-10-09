# RHMiniMaxH3DualSigmaSampler

## 节点类型

`RHMiniMaxH3DualSigmaSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 21 个 workflow 中。

## 输入

- `h3_model:MINIMAX_H3_DIRECT_MODEL`（21 次）
- `conditioning:MINIMAX_H3_CONDITIONING`（21 次）
- `av_latent:MINIMAX_H3_AV_LATENT`（21 次）
- `seed:INT`（21 次）
- `sigma_points:INT`（21 次）
- `video_shift:FLOAT`（21 次）
- `audio_shift:FLOAT`（21 次）
- `accel:COMBO`（21 次）
- `denoise_video:BOOLEAN`（21 次）
- `cache_dit_rdt:FLOAT`（21 次）

## 输出

- `sampled_av_latent:MINIMAX_H3_AV_LATENT`（21 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[42, "randomize", 50, 12.000000000000002, 3.0000000000000004, "manual-velocity", true, 0.12000000000000002, 2, 4, 4, "eu`（7 次）
- `[42, "fixed", 50, 12, 3, "manual-velocity", true, 0.12, 2, 4, 4, "euler", false]`（3 次）
- `[506867849533793, "randomize", 50, 12.000000000000002, 3.0000000000000004, "manual-velocity", true, 0.12000000000000002,`（3 次）
- `[718950812003780, "randomize", 50, 12.000000000000002, 3.0000000000000004, "manual-velocity", true, 0.12000000000000002,`（3 次）
- `[324835101933343, "randomize", 50, 12.000000000000002, 3.0000000000000004, "off", true, 0.12000000000000002, 2, 4, 4, "e`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
