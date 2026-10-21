---
key: 图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json
name: 写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json
hash: 86fe99aa124013c9
coverage: 0.846154
learned_at: 2026-10-19 22:15:53
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, UNETLoader, LayerUtility: PurgeVRAM V2, ImageScaleBy, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LayerUtility: PurgeVRAM V2, CLIPLoader, LoraLoaderModelOnly, ConditioningZeroOut, VAELoader, VAEDecode, VAEEncode, CLIPTextEncode, LayerFilter: HDREffects, KSamplerAdvanced, UNETLoader, PreviewImage, KSampler, VAEDecode, PreviewImage, SeedVR2VideoUpscaler, SaveImage, PreviewImage, easy textSwitch, easy showAnything, CR Text, RH_LLMAPI_Pro_Node, Note, CR Text, CR Text, EmptyLatentImage, Note, CLIPTextEncode, VAELoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2304, "sampler_name": "euler", "scheduler": "simple", "seed": 238606920380551, "steps": 6, "width": 1728}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerFilter: HDREffects`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `PreviewImage`
- `easy textSwitch`
- `easy showAnything`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `Note`
- `CR Text`
- `CR Text`
- `EmptyLatentImage` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `238606920380551`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1728`
- `height` = `2304`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`VAEEncode`、`LayerFilter: HDREffects`、`KSamplerAdvanced`、`KSampler`、`SeedVR2VideoUpscaler`、`SaveImage`、`easy textSwitch`、`CR Text`、`RH_LLMAPI_Pro_Node`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
