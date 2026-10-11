# BodyRatioMapperProportionTransfer

## 节点类型

`BodyRatioMapperProportionTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `pose_keypoint:POSE_KEYPOINT`（3 次）
- `ref_pose_keypoint:POSE_KEYPOINT`（3 次）
- `manual_anchor_pose:POSE_KEYPOINT`（3 次）
- `manual_first_frame:POSE_KEYPOINT`（3 次）
- `enable_rpca:BOOLEAN`（3 次）
- `hand_scaling:BOOLEAN`（3 次）
- `foot_scaling:BOOLEAN`（3 次）
- `offset_stabilizer_y:BOOLEAN`（3 次）
- `offset_stabilizer_x:BOOLEAN`（3 次）
- `best_hand_search:BOOLEAN`（3 次）

## 输出

- `changed_pose_keypoint:POSE_KEYPOINT`（3 次）
- `anchor_pose_keypoint:POSE_KEYPOINT`（3 次）
- `first_frame_output:POSE_KEYPOINT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, true, true, false, true, true, true, true, false, true, false, false, false, "single_frame_multi_person", f`（1 次）
- `[true, false, false, true, false, false, false, false, false, false, true, true, false, false, "single_frame_multi_perso`（1 次）
- `[true, true, true, true, true, true, false, false, false, false, true, false, false, false, "single_frame_multi_person",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
