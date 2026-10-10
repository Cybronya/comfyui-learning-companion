# SDPoseDrawKeypoints

## 节点类型

`SDPoseDrawKeypoints`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `keypoints:POSE_KEYPOINT`（3 次）
- `draw_body:BOOLEAN`（3 次）
- `draw_hands:BOOLEAN`（3 次）
- `draw_face:BOOLEAN`（3 次）
- `draw_feet:BOOLEAN`（3 次）
- `stick_width:INT`（3 次）
- `face_point_size:INT`（3 次）
- `score_threshold:FLOAT`（3 次）
- `draw_head:BOOLEAN`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, false, false, 4, 3, 0.3, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
