# MiniMaxH3StillConditioningT8

## 节点类型

`MiniMaxH3StillConditioningT8`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `video_vae:VAE`（3 次）
- `edit_image:IMAGE`（3 次）
- `ref_images.ref_image_0:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `canvas_mode:COMBO`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `target_mode:COMBO`（3 次）
- `reference_strength:FLOAT`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `av_latent:LATENT`（3 次）
- `conditioned_prompt:STRING`（3 次）
- `media_map_json:STRING`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Edit <Picture 1>: preserve the subject, composition, geometry, material details, lighting, and background. 女人做出比心的姿势",`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
