# workflow>CLIP视觉编码

## 节点类型

`workflow>CLIP视觉编码`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP视觉:CLIP_VISION`（1 次）
- `图像:IMAGE`（1 次）
- `CLIPVisionEncode clip_vision:CLIP_VISION`（1 次）
- `CLIPVisionEncode image:IMAGE`（1 次）
- `CLIPVisionEncode 2 clip_vision:CLIP_VISION`（1 次）
- `CLIPVisionEncode 2 image:IMAGE`（1 次）

## 输出

- `CLIP视觉输出:CLIP_VISION_OUTPUT`（1 次）
- `CLIPVisionEncode CLIP视觉输出:CLIP_VISION_OUTPUT`（1 次）
- `CLIPVisionEncode 2 CLIP视觉输出:CLIP_VISION_OUTPUT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", "none", "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
