# FaceDetailer

## 节点类型

`FaceDetailer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:MODEL`（3 次）
- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `bbox_detector:BBOX_DETECTOR`（3 次）
- `sam_model_opt:SAM_MODEL`（3 次）
- `segm_detector_opt:SEGM_DETECTOR`（3 次）
- `detailer_hook:DETAILER_HOOK`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `cropped_refined:IMAGE`（3 次）
- `cropped_enhanced_alpha:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `detailer_pipe:DETAILER_PIPE`（3 次）
- `cnet_images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, true, 1024, 42, "fixed", 6, 1, "res_2s", "beta", 0.25000000000000006, 5, true, true, 0.5, 10, 3, "center-1", 0, 0`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
