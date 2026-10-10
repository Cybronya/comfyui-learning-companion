# WanAnimatePlus ClipVisionEncode

## 节点类型

`WanAnimatePlus ClipVisionEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip_vision:CLIP_VISION`（1 次）
- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `negative_image:IMAGE`（1 次）
- `strength_1:FLOAT`（1 次）
- `strength_2:FLOAT`（1 次）
- `crop:COMBO`（1 次）
- `combine_embeds:COMBO`（1 次）
- `force_offload:BOOLEAN`（1 次）
- `tiles:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_CLIPEMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.0000000000000002, 1.0000000000000002, "disabled", "average", true, 0, 0.5000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
