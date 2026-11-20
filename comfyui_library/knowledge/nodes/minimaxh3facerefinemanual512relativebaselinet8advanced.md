# MiniMaxH3FaceRefineManual512RelativeBaselineT8Advanced

## 节点类型

`MiniMaxH3FaceRefineManual512RelativeBaselineT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `candidate_frames:IMAGE`（3 次）
- `face_plan:H3_T8_FACE_REFINE_PARITY_PLAN`（3 次）
- `latent_report_json:STRING`（3 次）
- `denoise_report_json:STRING`（3 次）
- `stitch_report_json:STRING`（3 次）
- `profile:COMBO`（3 次）
- `minimum_crop_face_height_px:FLOAT`（3 次）

## 输出

- `candidate_frames:IMAGE`（3 次）
- `baseline_report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["manual512_relative_author_parity_v2", 200]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
