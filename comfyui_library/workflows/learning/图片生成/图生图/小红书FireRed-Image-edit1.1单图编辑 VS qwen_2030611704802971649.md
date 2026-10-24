---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json
name: 小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json
hash: eb073b516d1b6535
coverage: 0.96
learned_at: 2026-10-23 12:49:14
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, SaveImage, PathchSageAttentionKJ, SaveImage, LoadImage, QwenImageIntegratedKSampler, QwenImageIntegratedKSampler, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, SaveImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, UNETLoader, CR Prompt Text, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 792761572029763, "sampler_name": 1472, "scheduler": 1104, "seed": "", "steps": "图生图 image-to-image"}
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json`

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
- `QwenImageIntegratedKSampler` ★核心
- `QwenImageIntegratedKSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `AddLabel`

## 关键参数

- `seed` = ``
- `steps` = `图生图 image-to-image`
- `cfg` = `1`
- `sampler_name` = `1472`
- `scheduler` = `1104`
- `denoise` = `792761572029763`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`QwenImageIntegratedKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Prompt Text`、`AddLabel`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、QwenImageIntegratedKSampler、CR Prompt Text、SaveImage
