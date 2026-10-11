# MiniMaxH3ScheduledReferenceToVideo

## 节点类型

`MiniMaxH3ScheduledReferenceToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `reference_schedule:H3_REFERENCE_SCHEDULE`（1 次）
- `state:H3_CHAIN_STATE`（1 次）
- `clip_index:INT`（1 次）
- `clip_count:INT`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `compiled_prompt:STRING`（1 次）
- `active_references:STRING`（1 次）
- `schedule_fingerprint:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subject_definitions:\n@style_base is the primary visual reference for <Subject 1>, defining the exact Classic Doom 199`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
