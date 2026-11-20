---
key: 平台全量/Wan2.1 风格转绘-首尾帧强控-深度&姿态双控_2038989648210432002.json
name: Wan2.1 风格转绘-首尾帧强控-深度&姿态双控_2038989648210432002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 风格转绘-首尾帧强控-深度&姿态双控_2038989648210432002.json
hash: 856b74b67da55e64
coverage: 0.882353
learned_at: 2026-11-14 01:04:32
nodes: [WanVideoApplyNAG, WanVideoSampler, WanVideoBlockSwap, WanVideoDecode, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, ImageResizeKJv2, WanVideoVACEEncode, WanVideoContextOptions, DWPreprocessor, PrimitiveInt, DepthAnythingV2Preprocessor, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, ImageFromBatch, ImageFromBatch, VAEDecode, CFGNorm, KSampler, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, FluxKontextImageScale, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, PreviewImage, WanVideoVACEEncode, KSampler, VAEDecode, PreviewImage, FluxKontextImageScale, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, PrimitiveStringMultiline, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoVAELoader, VHS_LoadVideo, PrimitiveInt, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 274210921930176, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.1 风格转绘-首尾帧强控-深度&姿态双控_2038989648210432002.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 风格转绘-首尾帧强控-深度&姿态双控_2038989648210432002.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`
- `WanVideoContextOptions`
- `DWPreprocessor`
- `PrimitiveInt`
- `DepthAnythingV2Preprocessor`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `ImageFromBatch`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextImageScale`
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `WanVideoVACEEncode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `274210921930176`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTextEncodeSingle`、`ImageResizeKJv2`、`WanVideoVACEEncode`、`WanVideoContextOptions`、`DWPreprocessor`、`DepthAnythingV2Preprocessor`、`WanVideoVACEStartToEndFrame`、`ImageFromBatch`、`VAEDecode`、`CFGNorm`、`KSampler`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`FluxKontextImageScale`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM V2`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、DepthAnythingV2Preprocessor、CFGNorm

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
