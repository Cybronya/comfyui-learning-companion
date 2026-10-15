# SCAIL2HeadTrackCrop

## 节点类型

`SCAIL2HeadTrackCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `full_body_video:IMAGE`（9 次）
- `head_masks:MASK`（9 次）
- `sam_model:MODEL`（9 次）
- `head_conditioning:CONDITIONING`（9 次）
- `crop_padding_ratio:FLOAT`（9 次）
- `square_align:INT`（9 次）
- `temporal_smoothing:FLOAT`（9 次）
- `mask_expand_px:INT`（9 次）
- `mask_blur_px:INT`（9 次）
- `sam_detection_threshold:FLOAT`（9 次）

## 输出

- `face_crop_video:IMAGE`（9 次）
- `crop_masks:MASK`（9 次）
- `crop_manifest:STRING`（9 次）
- `debug_preview:IMAGE`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 32, 0.6, 2, 1, 0.5, 1, 1, "fixed_canvas", "largest"]`（8 次）
- `[0, 32, 0.6, 2, 1, 0.5000000000000001, 1, 1, "fixed_canvas", "largest"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
