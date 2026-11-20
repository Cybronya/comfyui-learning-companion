# MiniMaxH3FaceRefineParityLatentT8Advanced

## 节点类型

`MiniMaxH3FaceRefineParityLatentT8Advanced`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `av_latent:LATENT`（3 次）
- `crops:IMAGE`（3 次）
- `video_vae:VAE`（3 次）
- `face_plan:H3_T8_FACE_REFINE_PARITY_PLAN`（3 次）
- `audio_policy:COMBO`（3 次）
- `allow_multi_shot_exp:BOOLEAN`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `av_latent:LATENT`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["require_locked", false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
