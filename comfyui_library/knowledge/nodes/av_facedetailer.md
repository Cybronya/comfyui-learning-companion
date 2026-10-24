# AV_FaceDetailer

## 节点类型

`AV_FaceDetailer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `bbox_detector:BBOX_DETECTOR`（1 次）
- `sam_model_opt:SAM_MODEL`（1 次）
- `segm_detector_opt:SEGM_DETECTOR`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `cropped_refined:IMAGE`（1 次）
- `cropped_enhanced_alpha:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `detailer_pipe:DETAILER_PIPE`（1 次）
- `cnet_images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 1024, 1122328285420766, "randomize", 6, 2, "dpmpp_sde", "karras", 0.7000000000000001, 5, true, true, 0.5, 10`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
