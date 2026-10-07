# HappyHorseVideoEditApi

## 节点类型

`HappyHorseVideoEditApi`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:VIDEO`（1 次）
- `model.reference_images.image1:IMAGE`（1 次）
- `model.reference_images.image2:IMAGE`（1 次）

## 输出

- `VIDEO:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["happyhorse-1.0-video-edit", "replace the woman in the video with the character in the image", "720P", "16:9", 14038944`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
