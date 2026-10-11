# SubtitleDetectorRapidOCR

## 节点类型

`SubtitleDetectorRapidOCR`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `ocr_mode:COMBO`（3 次）
- `model_type:COMBO`（3 次）
- `confidence_threshold:FLOAT`（3 次）
- `scale_factor:FLOAT`（3 次）
- `enhance_mode:COMBO`（3 次）
- `box_style:COMBO`（3 次）
- `skip_frames:INT`（3 次）
- `use_cuda:BOOLEAN`（3 次）
- `interpolate_mode:COMBO`（3 次）

## 输出

- `annotated_images:IMAGE`（3 次）
- `subtitle_mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["full", "MOBILE", 0.2, 0.8, "denoise_sharpen", "green_fill", 0, true, "union", 6]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
