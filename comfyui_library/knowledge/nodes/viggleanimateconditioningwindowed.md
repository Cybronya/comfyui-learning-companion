# ViggleAnimateConditioningWindowed

## 节点类型

`ViggleAnimateConditioningWindowed`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `cond_video:IMAGE`（1 次）
- `ref_image:IMAGE`（1 次）
- `text_cond:TEXT_COND`（1 次）
- `vae:VAE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `chunk_frames:INT`（1 次）
- `overlap_frames:INT`（1 次）
- `continuation:COMBO`（1 次）

## 输出

- `cond_set:VIGGLE_COND_SET`（1 次）
- `guider_positive:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 124, 22, "five_frame_anchor"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
