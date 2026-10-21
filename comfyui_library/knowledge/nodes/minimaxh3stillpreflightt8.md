# MiniMaxH3StillPreflightT8

## 节点类型

`MiniMaxH3StillPreflightT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `video_vae:VAE`（3 次）
- `edit_image:IMAGE`（3 次）
- `ref_images.ref_image_0:IMAGE`（3 次）
- `canvas_mode:COMBO`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `target_mode:COMBO`（3 次）
- `reference_strength:FLOAT`（3 次）
- `audio_target:COMBO`（3 次）

## 输出

- `ready:BOOLEAN`（3 次）
- `warning_count:INT`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["custom", 512, 512, "short_video_22_frames", 0.999, "generate_and_discard"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
