# VideoCubeTransitionNode

## 节点类型

`VideoCubeTransitionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（1 次）
- `video2:IMAGE`（1 次）
- `direction:COMBO`（1 次）
- `total_frames:INT`（1 次）
- `fps:INT`（1 次）
- `rotation_angle:FLOAT`（1 次）
- `cube_size:FLOAT`（1 次）
- `perspective:FLOAT`（1 次）
- `use_gpu:BOOLEAN`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["horizontal", 60, 24, 90, 300, 800, false, 5, "#000000", 640, 640]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
