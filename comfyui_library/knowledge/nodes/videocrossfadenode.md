# VideoCrossfadeNode

## 节点类型

`VideoCrossfadeNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（1 次）
- `video2:IMAGE`（1 次）
- `transition_mode:COMBO`（1 次）
- `total_frames:INT`（1 次）
- `fps:INT`（1 次）
- `background_color:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crossfade", 55, 24, "#FF0000", 640, 640]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
