# SCAIL2AlignReferenceFaceToCrop

## 节点类型

`SCAIL2AlignReferenceFaceToCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `face_crop_video:IMAGE`（9 次）
- `reference_image:IMAGE`（9 次）
- `target_frame_index:INT`（9 次）
- `face_scale:FLOAT`（9 次）
- `x_offset_ratio:FLOAT`（9 次）
- `y_offset_ratio:FLOAT`（9 次）
- `face_size_basis:COMBO`（9 次）
- `target_face_select:COMBO`（9 次）
- `reference_face_select:COMBO`（9 次）
- `padding_mode:COMBO`（9 次）

## 输出

- `aligned_reference_image:IMAGE`（9 次）
- `debug_preview:IMAGE`（9 次）
- `summary:STRING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, 0, 0, "bbox_width", "center", "largest", "edge", "buffalo_l", "auto", 640, "auto", "full_range", 0.5, "shift_insi`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
