# KlingVideoNode

## 节点类型

`KlingVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `start_frame:IMAGE`（2 次）
- `multi_shot.prompt:STRING`（1 次）

## 输出

- `VIDEO:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2 storyboards", "Ultra‑realistic boxing match inside a packed arena at night. Two muscular male boxers in bright trunk`（1 次）
- `["disabled", "", "", 5, true, "kling-v3", "1080p", "1:1", 757799685, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
