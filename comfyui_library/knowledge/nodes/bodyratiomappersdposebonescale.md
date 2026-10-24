# BodyRatioMapperSDPoseBoneScale

## 节点类型

`BodyRatioMapperSDPoseBoneScale`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pose_keypoint:POSE_KEYPOINT`（2 次）
- `person_idx:INT`（2 次）
- `scale_head_x:FLOAT`（2 次）
- `scale_head_y:FLOAT`（2 次）
- `scale_neck:FLOAT`（2 次）
- `scale_shoulder_width:FLOAT`（2 次）
- `scale_upper_arm:FLOAT`（2 次）
- `scale_lower_arm:FLOAT`（2 次）
- `scale_torso:FLOAT`（2 次）
- `scale_hip_width:FLOAT`（2 次）

## 输出

- `pose_keypoint:POSE_KEYPOINT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-1, 1, 1, 1, 1, 0.7, 0.7, 1, 1, 0.7, 0.7, 1, 0.6]`（1 次）
- `[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
