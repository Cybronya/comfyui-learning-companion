# VideoShakeTransitionNode

## 节点类型

`VideoShakeTransitionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（1 次）
- `video2:IMAGE`（1 次）
- `shake_style:COMBO`（1 次）
- `total_frames:INT`（1 次）
- `fps:INT`（1 次）
- `shake_intensity:FLOAT`（1 次）
- `shake_frequency:FLOAT`（1 次）
- `transition_point:FLOAT`（1 次）
- `fade_mix:BOOLEAN`（1 次）
- `use_gpu:BOOLEAN`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["random_shake", 12, 24, 20, 8, 0.5, true, false, 8, "#000000", 640, 640, 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
