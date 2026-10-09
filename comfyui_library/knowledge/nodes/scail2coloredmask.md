# SCAIL2ColoredMask

## 节点类型

`SCAIL2ColoredMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `driving_track_data:SAM3_TRACK_DATA`（1 次）
- `ref_track_data:SAM3_TRACK_DATA,MASK`（1 次）
- `object_indices:STRING`（1 次）
- `sort_by:COMBO`（1 次）
- `replacement_mode:BOOLEAN`（1 次）

## 输出

- `pose_video_mask:IMAGE`（1 次）
- `reference_image_mask:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "left_to_right", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
