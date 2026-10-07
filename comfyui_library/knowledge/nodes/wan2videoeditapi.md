# Wan2VideoEditApi

## 节点类型

`Wan2VideoEditApi`

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
- `model.reference_images.image3:IMAGE`（1 次）

## 输出

- `VIDEO:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.7-videoedit", "Replace the two elderly men with the bear from image1 and the dog from image2. The bear sits on th`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
