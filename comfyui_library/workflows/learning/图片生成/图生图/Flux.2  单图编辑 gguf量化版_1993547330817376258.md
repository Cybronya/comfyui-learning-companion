---
key: 图片生成/图生图/Flux.2  单图编辑 gguf量化版_1993547330817376258.json
name: Flux.2  单图编辑 gguf量化版_1993547330817376258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2  单图编辑 gguf量化版_1993547330817376258.json
hash: 21de56f4c2da1efe
coverage: 0.941176
learned_at: 2026-10-23 10:58:44
nodes: [CLIPLoader, VAELoader, Anything Everywhere, KSampler, ConditioningZeroOut, ReferenceLatent, ImageScaleToTotalPixels, VAEEncode, LoadImage, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, RH_Translator, UnetLoaderGGUF, PathchSageAttentionKJ, ModelPatchTorchSettings]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 112143292605429, "steps": 20}
---

# 图片生成/图生图/Flux.2  单图编辑 gguf量化版_1993547330817376258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2  单图编辑 gguf量化版_1993547330817376258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `RH_Translator`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `112143292605429`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageScaleToTotalPixels`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`RH_Translator`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、ReferenceLatent
