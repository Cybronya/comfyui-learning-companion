# Robust Video Matting

## 节点类型

`Robust Video Matting`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video_frames:IMAGE`（2 次）
- `backbone:COMBO`（1 次）
- `fp16:BOOLEAN`（1 次）
- `bg_color:STRING`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["resnet50", true, "green", 4]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
