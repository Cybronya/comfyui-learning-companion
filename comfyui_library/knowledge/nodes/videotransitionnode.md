# VideoTransitionNode

## 节点类型

`VideoTransitionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（3 次）
- `video2:IMAGE`（3 次）
- `transition_mode:COMBO`（3 次）
- `transition_frames:INT`（3 次）
- `target_width:INT`（3 次）
- `target_height:INT`（3 次）
- `length_mode:COMBO`（3 次）

## 输出

- `images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crossfade", 1, 0, 0, "overlap"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
