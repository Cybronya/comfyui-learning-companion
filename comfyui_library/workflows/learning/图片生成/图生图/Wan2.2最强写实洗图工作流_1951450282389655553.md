---
key: 图片生成/图生图/Wan2.2最强写实洗图工作流_1951450282389655553.json
name: Wan2.2最强写实洗图工作流_1951450282389655553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2最强写实洗图工作流_1951450282389655553.json
hash: 4ed55d17871a6ac0
coverage: 0.827586
learned_at: 2026-10-23 11:28:22
nodes: [CLIPTextEncode, VAEEncode, CLIPTextEncode, VAEDecode, ModelSamplingSD3, CLIPLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, CR Text Concatenate, RH_Captioner, PrimitiveStringMultiline, LoadImage, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, UNETLoader, UnetLoaderGGUF, LayerUtility: ImageScaleByAspectRatio V2, DF_Integer, PrimitiveFloat, KSampler, MaxNode, PrimitiveFloat, PrimitiveFloat, MinNode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 435275315490781, "steps": 20}
---

# 图片生成/图生图/Wan2.2最强写实洗图工作流_1951450282389655553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2最强写实洗图工作流_1951450282389655553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `RH_Captioner`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DF_Integer`
- `PrimitiveFloat`
- `KSampler` ★核心
- `MaxNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MinNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `435275315490781`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`ModelSamplingSD3`、`CLIPLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CR Text Concatenate`、`RH_Captioner`、`LoadImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`UNETLoader`、`UnetLoaderGGUF`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Integer`、`KSampler`、`MaxNode`、`MinNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
