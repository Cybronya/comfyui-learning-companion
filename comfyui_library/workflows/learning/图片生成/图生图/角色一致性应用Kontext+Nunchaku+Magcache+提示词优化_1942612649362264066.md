---
key: 图片生成/图生图/角色一致性应用Kontext+Nunchaku+Magcache+提示词优化_1942612649362264066.json
name: 角色一致性应用Kontext+Nunchaku+Magcache+提示词优化_1942612649362264066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色一致性应用Kontext+Nunchaku+Magcache+提示词优化_1942612649362264066.json
hash: 68286573129da429
coverage: 1
learned_at: 2026-10-23 13:26:20
nodes: [NunchakuFluxDiTLoader, VAELoader, RHHiddenNodes, RH_Translator, CLIPTextEncode, KSamplerSelect, BasicScheduler, RandomNoise, BasicGuider, ReferenceLatent, VAEEncode, CFGZeroStar, easy cleanGpuUsed, FluxGuidance, VAEDecode, EmptyLatentImage, ApplyFBCacheOnModel, ModelSamplingFlux, SamplerCustomAdvanced, Int, SaveImage, LoadImage, LoraLoaderModelOnly, DualCLIPLoader, CR Text, ImageResizeKJ, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/图生图/角色一致性应用Kontext+Nunchaku+Magcache+提示词优化_1942612649362264066.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色一致性应用Kontext+Nunchaku+Magcache+提示词优化_1942612649362264066.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `NunchakuFluxDiTLoader`
- `VAELoader`
- `RHHiddenNodes`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CFGZeroStar`
- `easy cleanGpuUsed`
- `FluxGuidance`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ApplyFBCacheOnModel`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `Int`
- `SaveImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `CR Text`
- `ImageResizeKJ`
- `Int`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`NunchakuFluxDiTLoader`、`VAELoader`、`RHHiddenNodes`、`RH_Translator`、`CLIPTextEncode`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`CFGZeroStar`、`easy cleanGpuUsed`、`FluxGuidance`、`VAEDecode`、`EmptyLatentImage`、`ApplyFBCacheOnModel`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`Int`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CR Text`、`ImageResizeKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect
