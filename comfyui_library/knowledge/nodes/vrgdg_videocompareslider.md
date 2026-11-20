# VRGDG_VideoCompareSlider

## 节点类型

`VRGDG_VideoCompareSlider`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `before_images:IMAGE`（1 次）
- `after_images:IMAGE`（1 次）
- `before_video:VHS_FILENAMES`（1 次）
- `after_video:VHS_FILENAMES`（1 次）
- `slider_position:FLOAT`（1 次）
- `before_label:STRING`（1 次）
- `after_label:STRING`（1 次）
- `show_labels:BOOLEAN`（1 次）
- `loop:BOOLEAN`（1 次）
- `muted:BOOLEAN`（1 次）

## 输出

- `before_video:VHS_FILENAMES`（1 次）
- `after_video:VHS_FILENAMES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "一采", "二采", true, true, false, 5, "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
