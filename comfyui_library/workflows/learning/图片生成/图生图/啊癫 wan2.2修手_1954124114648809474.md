---
key: 图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json
name: 啊癫 wan2.2修手_1954124114648809474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json
hash: c7ad32c10d77d2a0
coverage: 0.973684
learned_at: 2026-10-23 12:37:08
nodes: [LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, JWInteger, JWInteger, JWInteger, JWInteger, PDIMAGE_LongerSize, CLIPLoader, InpaintModelConditioning, CLIPTextEncode, JWInteger, CLIPTextEncode, PreviewImage, ImagePadKJ, MaskPreview+, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UnetLoaderGGUF, UnetLoaderGGUF, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ModelSamplingSD3, KSampler, Bjornulf_TextToStringAndSeed, VAEDecode, KSampler, VAEDecode, ImageConcanate, LoadImage, SaveImage, SaveImage, SaveImage, PMRF, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 102848737037771, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `PDIMAGE_LongerSize`
- `CLIPLoader`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImagePadKJ`
- `MaskPreview+`
- `MaskPreview+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `Bjornulf_TextToStringAndSeed`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PMRF`
- `SaveImage`

## 关键参数

- `seed` = `102848737037771`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`JWInteger`、`PDIMAGE_LongerSize`、`CLIPLoader`、`InpaintModelConditioning`、`CLIPTextEncode`、`ImagePadKJ`、`MaskPreview+`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LayerUtility: PurgeVRAM`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`ImageConcanate`、`LoadImage`、`SaveImage`、`PMRF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、Bjornulf_TextToStringAndSeed

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
