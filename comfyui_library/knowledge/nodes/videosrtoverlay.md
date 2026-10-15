# VideoSrtOverlay

## 节点类型

`VideoSrtOverlay`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `srt_string:STRING`（2 次）
- `font_family:COMBO`（2 次）
- `font_size:INT`（2 次）
- `font_color:STRING`（2 次）
- `border_color:STRING`（2 次）
- `border_size:INT`（2 次）
- `shadow_color:STRING`（2 次）
- `shadow_size:INT`（2 次）
- `shadow_offset_x:INT`（2 次）

## 输出

- `images_with_subtitle:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "华文仿宋.ttf", 36, "#FFFFFF", "#000000", 3, "#000000", 1, 1, 2, "none", 150, 150, 0.82, 0.1, 24]`（1 次）
- `["", "华文仿宋.ttf", 44, "#FFD54F", "#111111", 5, "#000000", 2, 1, 2, "none", 150, 150, 0.25, 0.08, 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
