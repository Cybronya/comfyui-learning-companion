# SCAIL2IdentityTracker

## 节点类型

`SCAIL2IdentityTracker`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `sam3_model:MODEL`（2 次）
- `reference_image:IMAGE`（2 次）
- `pose_video:IMAGE`（2 次）
- `reference_conditioning:CONDITIONING`（2 次）
- `driving_conditioning:CONDITIONING`（2 次）
- `refine_iterations:INT`（2 次）
- `auto_detect:BOOLEAN`（2 次）
- `detection_threshold:FLOAT`（2 次）
- `detect_interval:INT`（2 次）
- `markers:STRING`（2 次）

## 输出

- `ref_track_data:SAM3_TRACK_DATA`（2 次）
- `driving_track_data:SAM3_TRACK_DATA`（2 次）
- `reference_image:IMAGE`（2 次）
- `pose_video:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, true, 0.5, 1, "{\"reference\":[{\"type\":\"point\",\"points\":[[411.89248136342326,518.3545822621851,1],[415.3156909`（1 次）
- `[2, true, 0.5, 1, "{\"reference\":[],\"driving\":[{\"type\":\"point\",\"points\":[[329.36102009811697,383.41875870216444`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
