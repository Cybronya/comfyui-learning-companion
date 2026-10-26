# MiniMaxH3VideoMerge

## 节点类型

`MiniMaxH3VideoMerge`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images_b:IMAGE`（4 次）
- `images_a:IMAGE`（4 次）
- `audio_a:AUDIO`（4 次）
- `audio_b:AUDIO`（4 次）
- `seam_smooth:INT`（4 次）
- `blend_frames:INT`（4 次）
- `color_match:COMBO`（4 次）
- `fps:FLOAT`（4 次）

## 输出

- `images:IMAGE`（4 次）
- `audio:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "disabled", 24]`（2 次）
- `[1, 0, "seam_fade", 24]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
