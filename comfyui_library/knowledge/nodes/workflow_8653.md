# workflow>功能模块

## 节点类型

`workflow>功能模块`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `条件:CONDITIONING`（1 次）
- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `pwd:STRING`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）

## 输出

- `p0:*`（1 次）
- `CLIP:CLIP`（1 次）
- `RHHiddenNodes p0:*`（1 次）
- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-kontext-dev-fp8-e4m3fn.safetensors", "default", "ae.sft", "", "ViT-L-14-TEXT-detail-improved-hiT-GmP-HF.safetens`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
