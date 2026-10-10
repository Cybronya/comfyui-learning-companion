# WanVideoUniAnimatePoseInput

## 节点类型

`WanVideoUniAnimatePoseInput`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pose_images:IMAGE`（2 次）
- `reference_pose_image:IMAGE`（2 次）
- `strength:FLOAT`（2 次）
- `start_percent:FLOAT`（2 次）
- `end_percent:FLOAT`（2 次）

## 输出

- `unianimate_poses:UNIANIMATE_POSE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
