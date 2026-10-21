# VideoCaptionNode

## 节点类型

`VideoCaptionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_frames:IMAGE`（1 次）
- `video:VIDEO`（1 次）

## 输出

- `caption_text:STRING`（1 次）
- `preview_frames:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["视频复刻与重构", false, "", "", "Auto (Uniform)", 5, "", "智谱/glm-4-flash-250414", true, 1094031556894198, "randomize", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
