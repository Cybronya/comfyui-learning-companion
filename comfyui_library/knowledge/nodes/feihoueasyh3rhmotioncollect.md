# FeiHouEasyH3RHMotionCollect

## 节点类型

`FeiHouEasyH3RHMotionCollect`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent:LATENT`（2 次）
- `motion_state:FEIHOU_H3_MOTION_STATE`（2 次）
- `audio_output:COMBO`（2 次）
- `auto_queue:BOOLEAN`（2 次）
- `color_match:BOOLEAN`（2 次）
- `save_segments:BOOLEAN`（2 次）
- `filename_prefix:STRING`（2 次）
- `color_match_strength:FLOAT`（2 次）

## 输出

- `images:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `generated_audio:AUDIO`（2 次）
- `series_latent:LATENT`（2 次）
- `fps:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["自动", true, false, false, "FeiHou_H3_motion/segment", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
