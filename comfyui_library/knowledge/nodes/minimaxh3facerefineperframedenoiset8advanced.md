# MiniMaxH3FaceRefinePerFrameDenoiseT8Advanced

## 节点类型

`MiniMaxH3FaceRefinePerFrameDenoiseT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `av_latent:LATENT`（3 次）
- `face_plan:H3_T8_FACE_REFINE_PARITY_PLAN`（3 次）
- `strength_small_face:FLOAT`（3 次）
- `strength_large_face:FLOAT`（3 次）
- `scale_mode:COMBO`（3 次）
- `face_px_small:FLOAT`（3 次）
- `face_px_large:FLOAT`（3 次）
- `gamma:FLOAT`（3 次）
- `smooth_frames:INT`（3 次）
- `video_mask_mode:COMBO`（3 次）

## 输出

- `av_latent:LATENT`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.8, 0.35, "relative_to_clip", 30, 120, 1, 9, "replace_video_parity", true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
