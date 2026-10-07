# GeminiImage2Node

## 节点类型

`GeminiImage2Node`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 23 个 workflow 中。

## 输入

- `images:IMAGE`（34 次）
- `files:GEMINI_INPUT_FILES`（34 次）
- `prompt:STRING`（7 次）
- `aspect_ratio:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（34 次）
- `STRING:STRING`（34 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["upscale this image. refine details. preserve text. retain composition. refine textures, skin and materials.", "gemini-`（2 次）
- `["Create an orthographic blueprint that describes this building in plan, elevation and section.\n\n\n\n\n", "gemini-3-pr`（1 次）
- `["A miniature architectural scale model of a purple house, carefully crafted with clean edges and subtle textures. The m`（1 次）
- `["Orthographic character sheet, full body turnaround views, showing the exact same robot from a front view, left side vi`（1 次）
- `["Have the suit corresponding to this character strike a casual and fashionable pose", "gemini-3-pro-image-preview", 394`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
