---
key: 图片生成/图生图/FireRed-Image-Edit-1.1双图编辑_2034921732838002690.json
name: FireRed-Image-Edit-1.1双图编辑_2034921732838002690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1双图编辑_2034921732838002690.json
hash: f6dbadcb5ae7a87f
coverage: 0.848485
learned_at: 2026-10-23 10:55:43
nodes: [Anything Everywhere3, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, KSampler, VAEDecode, LoadImage, view_bridge_image, SaveImage, KSampler, VAEDecode, SaveImage, LoadImage, PreviewImage, ConditioningZeroOut, ToBinaryMask, PreviewImage, ConditioningZeroOut, ToBinaryMask, MaskFillHoles, LayerUtility: CropByMask, MaskFillHoles, LayerUtility: CropByMask, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio, LoadImage, easy seed, TextEncodeQwenImageEditPlusPro_lrzjason, JjkText, JjkText, TextEncodeQwenImageEditPlusPro_lrzjason]
patterns: []
missing: []
parameters: {"cfg": 1.2, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 599672064129147, "steps": 10}
---

# 图片生成/图生图/FireRed-Image-Edit-1.1双图编辑_2034921732838002690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1双图编辑_2034921732838002690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `Anything Everywhere3`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `view_bridge_image`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `ToBinaryMask`
- `PreviewImage`
- `ConditioningZeroOut`
- `ToBinaryMask`
- `MaskFillHoles`
- `LayerUtility: CropByMask`
- `MaskFillHoles`
- `LayerUtility: CropByMask`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `easy seed`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `JjkText`
- `JjkText`
- `TextEncodeQwenImageEditPlusPro_lrzjason`

## 关键参数

- `seed` = `599672064129147`
- `steps` = `10`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`VAEDecode`、`LoadImage`、`view_bridge_image`、`SaveImage`、`ConditioningZeroOut`、`ToBinaryMask`、`MaskFillHoles`、`LayerUtility: CropByMask`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio`、`easy seed`、`TextEncodeQwenImageEditPlusPro_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
