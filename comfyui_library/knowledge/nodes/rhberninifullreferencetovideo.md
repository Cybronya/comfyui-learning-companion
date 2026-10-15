# RHBerniniFullReferenceToVideo

## 节点类型

`RHBerniniFullReferenceToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `reference_image:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `negative_prompt:STRING`（3 次）
- `num_frames:INT`（3 次）
- `fps:INT`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `steps:INT`（3 次）
- `seed:INT`（3 次）
- `quality_preset:COMBO`（3 次）

## 输出

- `video:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The marble statue from image0, wearing the black T-shirt from image2, the tropical floral shorts from image3, and the `（1 次）
- `["The marble statue from image0, wearing the black T-shirt from image2, the tropical floral shorts from image3, and the `（1 次）
- `["", "low quality, blurry, distorted, text, watermark, jitter, flicker", 49, 16, 848, 480, 40, 1471621095, "randomize", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
