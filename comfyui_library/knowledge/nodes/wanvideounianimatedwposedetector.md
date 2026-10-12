# WanVideoUniAnimateDWPoseDetector

## 节点类型

`WanVideoUniAnimateDWPoseDetector`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `pose_images:IMAGE`（16 次）
- `reference_pose_image:IMAGE`（16 次）

## 输出

- `poses:IMAGE`（16 次）
- `reference_pose:IMAGE`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.3, 4, true, 4, true, true, 4, "RGB", "empty"]`（8 次）
- `[0.3]`（4 次）
- `[0.25000000000000006, 4, true, 4, true, true, 4, "RGB", "empty"]`（2 次）
- `[0.30000000000000004, 4, true, 4, true, true, 4, "RGB", "empty"]`（1 次）
- `[0.5000000000000001, 4, true, 4, true, true, 4, "RGB", "empty", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
