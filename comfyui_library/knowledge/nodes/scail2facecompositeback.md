# SCAIL2FaceCompositeBack

## 节点类型

`SCAIL2FaceCompositeBack`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `full_body_video:IMAGE`（9 次）
- `refined_face_video:IMAGE`（9 次）
- `crop_masks:MASK`（9 次）
- `crop_manifest:STRING`（9 次）
- `feather_px:INT`（9 次）
- `mask_contract_px:INT`（9 次）
- `color_correction:BOOLEAN`（9 次）
- `color_match_method:COMBO`（9 次）
- `face_fit_mode:COMBO`（9 次）
- `frame_mismatch_mode:COMBO`（9 次）

## 输出

- `frames:IMAGE`（9 次）
- `summary:STRING`（9 次）
- `debug_preview:IMAGE`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 0, true, "local_mean_std", "stretch", "trim_to_shortest", 0, "bilinear", 0, 0]`（8 次）
- `[2, 0, true, "local_mean_std", "stretch", "trim_to_shortest", 0, "bilinear", -1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
