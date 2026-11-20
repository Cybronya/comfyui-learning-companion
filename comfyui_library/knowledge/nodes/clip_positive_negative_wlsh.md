# CLIP Positive-Negative (WLSH)

## 节点类型

`CLIP Positive-Negative (WLSH)`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Guochao(style),distant mountains,landscape,clouds,sky,dark purple background,", "monochrome"]`（1 次）
- `["Main building,", "embedding:easynegative, "]`（1 次）
- `["Main building,,clouds, sky, mountains,,sfw, (masterpieces:1,2), best quality, masterpieces, high resolution, original,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
