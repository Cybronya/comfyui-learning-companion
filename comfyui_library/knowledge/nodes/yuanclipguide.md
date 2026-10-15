# YuanClipGuide

## 节点类型

`YuanClipGuide`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `模型:MODEL`（3 次）
- `正向条件:CONDITIONING`（3 次）
- `负向条件:CONDITIONING`（3 次）
- `VAE:VAE`（3 次）
- `潜空间:LATENT`（3 次）
- `引导数据:YUAN_CLIP_GUIDE_DATA`（3 次）
- `运动引导数据:YUAN_CLIP_MOTION_GUIDE_DATA`（3 次）
- `IC_LORA参数:IC_LORA_PARAMETERS`（3 次）
- `图像注意力强度:FLOAT`（3 次）

## 输出

- `模型:MODEL`（3 次）
- `正向条件:CONDITIONING`（3 次）
- `负向条件:CONDITIONING`（3 次）
- `潜空间:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
