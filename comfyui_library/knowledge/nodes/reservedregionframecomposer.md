# ReservedRegionFrameComposer

## 节点类型

`ReservedRegionFrameComposer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（2 次）
- `face_sequence:FACE_SEQUENCE`（2 次）
- `face_images:IMAGE`（2 次）
- `region_position:COMBO`（2 次）
- `region_size_px:INT`（2 次）
- `face_distribution:COMBO`（2 次）
- `interval_frames:INT`（2 次）
- `overflow_mode:COMBO`（2 次）
- `stack_direction:COMBO`（2 次）
- `face_scale_pct:FLOAT`（2 次）

## 输出

- `frames_out:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["left", 256, "one_face_per_interval", 12, "loop", "auto", 90, 12, 12, "center", "center", 0, 255, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
