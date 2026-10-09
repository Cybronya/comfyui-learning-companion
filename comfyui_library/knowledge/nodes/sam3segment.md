# SAM3Segment

## 节点类型

`SAM3Segment`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `output_mode:COMBO`（2 次）
- `confidence_threshold:FLOAT`（2 次）
- `max_segments:INT`（2 次）
- `segment_pick:INT`（2 次）
- `mask_blur:INT`（2 次）
- `mask_offset:INT`（2 次）
- `device:COMBO`（2 次）
- `invert_output:BOOLEAN`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `MASK_IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face", "Merged", 0.3, 1, 0, 0, 0, "Auto", false, false, "Alpha", "#222222"]`（1 次）
- `["face", "Merged", 0.30000000000000004, 1, 0, 0, 0, "Auto", false, false, "Alpha", "#222222"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
