---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json
name: 小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json
hash: 93f971daa60609b9
coverage: 0.96
learned_at: 2026-10-23 12:49:17
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, SaveImage, PathchSageAttentionKJ, SaveImage, LoadImage, UNETLoader, QwenImageIntegratedKSampler, QwenImageIntegratedKSampler, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, LayerUtility: ImageReel, SaveImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, CR Prompt Text, LoadImage, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 929698202775659, "sampler_name": 1472, "scheduler": 1104, "seed": "", "steps": "图生图 image-to-image"}
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（25 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `PathchSageAttentionKJ`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `QwenImageIntegratedKSampler` ★核心
- `QwenImageIntegratedKSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `LayerUtility: ImageReel`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `AddLabel`

## 关键参数

- `seed` = ``
- `steps` = `图生图 image-to-image`
- `cfg` = `1`
- `sampler_name` = `1472`
- `scheduler` = `1104`
- `denoise` = `929698202775659`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`QwenImageIntegratedKSampler`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`LayerUtility: ImageReel`、`CR Prompt Text`、`AddLabel`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、QwenImageIntegratedKSampler、CR Prompt Text、SaveImage
