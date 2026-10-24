---
key: 图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json
name: QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json
hash: 8e05808c93f867bd
coverage: 0.954545
learned_at: 2026-10-23 11:20:32
nodes: [QwenEditOutputExtractor, VAEDecode, CompressImages, UNETLoader, CFGNorm, ImageScaleBy, CropWithPadInfo, QwenEditConfigPreparer, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlusCustom_lrzjason, FluxKontextMultiReferenceLatentMethod, KSampler, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoadImage, CheckpointLoaderSimple, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenEditAdaptiveLongestEdge]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "new_Qwen-Rapid-AIO-NSFW-v19.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 391002861200863, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEditUtils 2.2 Optional Mask (1)_1992579715970166785.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（22 个）：
- `QwenEditOutputExtractor`
- `VAEDecode` ★核心
- `CompressImages`
- `UNETLoader` ★核心
- `CFGNorm`
- `ImageScaleBy`
- `CropWithPadInfo`
- `QwenEditConfigPreparer`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenEditAdaptiveLongestEdge`

## 关键参数

- `seed` = `391002861200863`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `new_Qwen-Rapid-AIO-NSFW-v19.safetensors`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`QwenEditOutputExtractor`、`VAEDecode`、`CompressImages`、`UNETLoader`、`CFGNorm`、`ImageScaleBy`、`CropWithPadInfo`、`QwenEditConfigPreparer`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`KSampler`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`LoadImage`、`CheckpointLoaderSimple`、`QwenEditAdaptiveLongestEdge`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、LoadImage、CFGNorm、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
