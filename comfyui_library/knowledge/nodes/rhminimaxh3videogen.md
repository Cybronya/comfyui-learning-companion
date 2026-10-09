# RHMiniMaxH3VideoGen

## 节点类型

`RHMiniMaxH3VideoGen`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `h3_model:MINIMAX_H3_DIRECT_MODEL`（7 次）
- `h3_text_encoder:MINIMAX_H3_TEXT_ENCODER`（7 次）
- `h3_vae_bundle:MINIMAX_H3_VAE_BUNDLE`（7 次）
- `first_frame:IMAGE`（7 次）
- `last_frame:IMAGE`（7 次）
- `source_video:VIDEO`（7 次）
- `sampler_config:MINIMAX_H3_SAMPLER_CONFIG`（7 次）
- `prompt:STRING`（7 次）
- `aspect_ratio:COMBO`（7 次）
- `width:INT`（7 次）

## 输出

- `frames:IMAGE`（7 次）
- `audio:AUDIO`（7 次）
- `av_latent:MINIMAX_H3_AV_LATENT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "16:9", 832, 480, 5, 42, "randomize", 4, 12, 3, "res_multistep", "auto", false, "auto"]`（5 次）
- `["768P", "16:9", 832, 480, 5, 42, "randomize", 4, 12, 3, "res_multistep", "auto", false, "auto"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
