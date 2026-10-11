# Add Subtitles To Frames

## 节点类型

`Add Subtitles To Frames`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `alignment:whisper_alignment`（1 次）
- `y_position:INT`（1 次）
- `video_fps:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `cropped_subtitles:IMAGE`（1 次）
- `subtitle_coord:subtitle_coord`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["white", "Microsoft_YaHei_Bold.ttf", 50, 100, 100, true, false, 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
