# VideoCubeRotationAdvancedNode

## 节点类型

`VideoCubeRotationAdvancedNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_front:IMAGE`（1 次）
- `video_back:IMAGE`（1 次）
- `video_left:IMAGE`（1 次）
- `video_right:IMAGE`（1 次）
- `video_top:IMAGE`（1 次）
- `video_bottom:IMAGE`（1 次）
- `rotation_style:COMBO`（1 次）
- `rotation_speed:FLOAT`（1 次）
- `duration:FLOAT`（1 次）
- `fps:INT`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["diagonal", 1, 5, 30, "#1a1a2e", 640, 640, 0.6, 1000]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
