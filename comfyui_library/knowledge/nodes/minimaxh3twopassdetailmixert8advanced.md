# MiniMaxH3TwoPassDetailMixerT8Advanced

## 节点类型

`MiniMaxH3TwoPassDetailMixerT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `model:MODEL`（14 次）
- `av_latent:LATENT`（14 次）
- `refine_sigmas:SIGMAS`（14 次）
- `shift_video:FLOAT`（14 次）
- `shift_audio:FLOAT`（14 次）
- `enable_tail:BOOLEAN`（14 次）
- `extra_tail_steps:INT`（14 次）
- `tail_spacing:COMBO`（14 次）
- `enable_model_time_bias:BOOLEAN`（14 次）
- `bias:FLOAT`（14 次）

## 输出

- `model:MODEL`（14 次）
- `sampler:SAMPLER`（14 次）
- `sigmas:SIGMAS`（14 次）
- `actual_nfe:INT`（14 次）
- `planned_joint_av_forwards:INT`（14 次）
- `report_json:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12, 3, false, 1, "video_sigma_linear", false, -0.025, 0.7, 0.95, "video_sigma", false, 0.35, "25", 0.25, 0.85, false, 0`（2 次）
- `[12, 3, false, 1, "video_sigma_linear", false, -0.025, 0.7, 0.95, "video_sigma", false, 0.35, "25", 0.25, 0.85, false, 0`（2 次）
- `[12, 3, false, 1, "video_sigma_linear", false, -0.025, 0.7, 0.95, "video_sigma", false, 0.35, "25", 0.25, 0.85, false, 0`（1 次）
- `[12, 3, false, 1, "video_sigma_linear", false, -0.025, 0.7, 0.95, "video_sigma", false, 0.35, "25", 0.25, 0.85, false, 0`（1 次）
- `[12, 3, false, 1, "video_sigma_linear", false, -0.025, 0.7, 0.95, "video_sigma", false, 0.35, "25", 0.25, 0.85, false, 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
