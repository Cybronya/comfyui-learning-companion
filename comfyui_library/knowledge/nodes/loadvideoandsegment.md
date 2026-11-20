# LoadVideoAndSegment_

## 节点类型

`LoadVideoAndSegment_`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `scenes_video:SCENE_VIDEO`（2 次）
- `scenes_count:INT`（2 次）
- `frame_count:INT`（2 次）
- `fps:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["video/a6a52794c9a7c479dfdb6c68b925e84573d6004206bcfe6eb10f795946d8d71a.mp4", 10, 0, null, "video", "image", ""]`（1 次）
- `["7月24日(6).mp4", -1, 0, null, "video", "image", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
