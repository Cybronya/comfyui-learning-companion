# MiniMaxH3LongVideoInNodeLoopEffectsT8Advanced

## 节点类型

`MiniMaxH3LongVideoInNodeLoopEffectsT8Advanced`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `prompt_relay_plan:H3_T8_PROMPT_RELAY_PLAN`（1 次）
- `drive_audio:AUDIO`（1 次）
- `final_audio:AUDIO`（1 次）
- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `persistent_identity_image:IMAGE`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_path:STRING`（1 次）
- `manifest_path:STRING`（1 次）
- `completed_segments:INT`（1 次）
- `status:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["h3_dialogue_aligned_stock20_24s_manual_second_pass_v1", 25.290000000000006, 736, 416, 124, 39, "", "", "apply_exp", 25`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
