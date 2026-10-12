# VideoBlinkTransitionNode

## 节点类型

`VideoBlinkTransitionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（1 次）
- `video2:IMAGE`（1 次）
- `total_frames:INT`（1 次）
- `fps:INT`（1 次）
- `blink_speed:FLOAT`（1 次）
- `blur_intensity:FLOAT`（1 次）
- `eyelid_curve:FLOAT`（1 次）
- `edge_feather:FLOAT`（1 次）
- `mask_color:COMBO`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[60, 30, 1, 0.8, 0.3, 0.2, "black"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
