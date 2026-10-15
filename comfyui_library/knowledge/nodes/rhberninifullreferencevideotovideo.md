# RHBerniniFullReferenceVideoToVideo

## 节点类型

`RHBerniniFullReferenceVideoToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video:VIDEO`（2 次）
- `reference_image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `negative_prompt:STRING`（2 次）
- `num_frames:INT`（2 次）
- `fps:INT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `steps:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Replace the person's outer shirt with the shirt from the reference image while keeping the inner undershirt unchanged,`（1 次）
- `["", "low quality, blurry, distorted, text, watermark, jitter, flicker", 49, 16, 0, 0, 49, 675523225, "randomize", "stan`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
