# SDPoseOODProcessor

## 节点类型

`SDPoseOODProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sdpose_model:SDPOSE_MODEL`（1 次）
- `images:IMAGE`（1 次）
- `data_from_florence2:JSON`（1 次）
- `grounding_dino_model:GROUNDING_DINO_MODEL`（1 次）
- `yolo_model:YOLO_MODEL`（1 次）
- `score_threshold:FLOAT`（1 次）
- `overlay_alpha:FLOAT`（1 次）
- `batch_size:INT`（1 次）
- `prompt:STRING`（1 次）
- `gd_threshold:FLOAT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `pose_keypoint:POSE_KEYPOINT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.3, 1, 1, "person .", 0.3, false, "poses/pose_edit", true, true, true, false, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
