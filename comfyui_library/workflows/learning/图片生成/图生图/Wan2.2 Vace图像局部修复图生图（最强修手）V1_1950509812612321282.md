---
key: 图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json
name: Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json
hash: 5f63a53a04b63f52
coverage: 0.972973
learned_at: 2026-10-23 11:28:00
nodes: [LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, JWInteger, JWInteger, JWInteger, JWInteger, PDIMAGE_LongerSize, CLIPLoader, InpaintModelConditioning, CLIPTextEncode, JWInteger, CLIPTextEncode, PreviewImage, ImagePadKJ, MaskPreview+, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UnetLoaderGGUF, UnetLoaderGGUF, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ModelSamplingSD3, SaveImage, KSampler, Bjornulf_TextToStringAndSeed, SaveImage, VAEDecode, KSampler, VAEDecode, PMRF, SaveImage, ImageConcanate]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 523897563824499, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `LoadImage`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `SaveImage`
- `KSampler` ★核心
- `Bjornulf_TextToStringAndSeed`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PMRF`
- `SaveImage`
- `ImageConcanate`

## 关键参数

- `seed` = `523897563824499`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`JWInteger`、`PDIMAGE_LongerSize`、`CLIPLoader`、`InpaintModelConditioning`、`CLIPTextEncode`、`ImagePadKJ`、`MaskPreview+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LayerUtility: PurgeVRAM`、`SaveImage`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`PMRF`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、Bjornulf_TextToStringAndSeed

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
