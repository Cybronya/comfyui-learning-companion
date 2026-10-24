---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json
name: 小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json
hash: 1a67022aeae56371
coverage: 0.925926
learned_at: 2026-10-23 12:49:18
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, SaveImage, PathchSageAttentionKJ, QwenImageIntegratedKSampler, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, SaveImage, LayerUtility: ImageReelComposit, LoadImage, LoadImage, UNETLoader, LayerUtility: ImageReel, LayerUtility: ImageReel, SaveImage, LoadImage, CR Prompt Text, QwenImageIntegratedKSampler, Note, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 688615941309839, "sampler_name": 1472, "scheduler": 1104, "seed": "", "steps": "图生图 image-to-image"}
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `PathchSageAttentionKJ`
- `QwenImageIntegratedKSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReel`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `QwenImageIntegratedKSampler` ★核心
- `Note`
- `AddLabel`

## 关键参数

- `seed` = ``
- `steps` = `图生图 image-to-image`
- `cfg` = `1`
- `sampler_name` = `1472`
- `scheduler` = `1104`
- `denoise` = `688615941309839`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`QwenImageIntegratedKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`LoadImage`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`CR Prompt Text`、`AddLabel`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、QwenImageIntegratedKSampler、CR Prompt Text、SaveImage
