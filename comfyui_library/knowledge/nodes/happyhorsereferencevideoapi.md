# HappyHorseReferenceVideoApi

## 节点类型

`HappyHorseReferenceVideoApi`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model.reference_images.image1:IMAGE`（2 次）
- `model.reference_images.image2:IMAGE`（2 次）
- `model.reference_images.image3:IMAGE`（2 次）

## 输出

- `VIDEO:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["happyhorse-1.0-r2v", "Video Prompt: Based on the male character in @image2 and the red vintage sports car in reference`（1 次）
- `["happyhorse-1.1-r2v", "Base Parameter Constraints: No subtitles, No background music, consistent lighting, no visual cl`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
