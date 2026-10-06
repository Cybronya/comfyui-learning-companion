# MiniMaxH3FaceRefineConditioningT8Advanced

## 节点类型

`MiniMaxH3FaceRefineConditioningT8Advanced`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `av_latent:LATENT`（2 次）
- `crops:IMAGE`（2 次）
- `video_vae:VAE`（2 次）
- `face_plan:H3_T8_FACE_REFINE_PLAN`（2 次）
- `audio_policy:COMBO`（2 次）
- `allow_multi_shot_exp:BOOLEAN`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `av_latent:LATENT`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["preserve_existing", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
