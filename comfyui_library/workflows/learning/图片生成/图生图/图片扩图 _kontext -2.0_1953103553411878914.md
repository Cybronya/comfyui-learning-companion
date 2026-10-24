---
key: 图片生成/图生图/图片扩图 _kontext -2.0_1953103553411878914.json
name: 图片扩图 _kontext -2.0_1953103553411878914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片扩图 _kontext -2.0_1953103553411878914.json
hash: 03656e70d33adcc9
coverage: 0.846154
learned_at: 2026-10-23 12:40:52
nodes: [UNETLoader, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, FluxKontextImageScale, LoraLoaderModelOnly, ModelSamplingFlux, VAELoader, DualCLIPLoader, Anything Everywhere3, CLIPTextEncode, BasicScheduler, BasicGuider, FluxGuidance, ReferenceLatent, LayerUtility: PurgeVRAM V2, PreviewImage, LoadImage, GetImageSize+, VAEEncode, Anything Everywhere, Anything Everywhere, JWImageResizeByShorterSide, VAEDecode, SaveImage, ImagePadForOutpaintMasked_UTK]
patterns: []
missing: []
---

# 图片生成/图生图/图片扩图 _kontext -2.0_1953103553411878914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片扩图 _kontext -2.0_1953103553411878914.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `FluxKontextImageScale`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingFlux`
- `VAELoader`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `BasicGuider`
- `FluxGuidance`
- `ReferenceLatent`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `LoadImage`
- `GetImageSize+`
- `VAEEncode` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `JWImageResizeByShorterSide`
- `VAEDecode` ★核心
- `SaveImage`
- `ImagePadForOutpaintMasked_UTK`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`UNETLoader`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`ModelSamplingFlux`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`BasicScheduler`、`BasicGuider`、`FluxGuidance`、`ReferenceLatent`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`GetImageSize+`、`VAEEncode`、`JWImageResizeByShorterSide`、`VAEDecode`、`SaveImage`、`ImagePadForOutpaintMasked_UTK`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
