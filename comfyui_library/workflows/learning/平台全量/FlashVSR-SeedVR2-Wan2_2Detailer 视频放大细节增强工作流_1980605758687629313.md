---
key: 平台全量/FlashVSR-SeedVR2-Wan2_2Detailer 视频放大细节增强工作流_1980605758687629313.json
name: FlashVSR-SeedVR2-Wan2_2Detailer 视频放大细节增强工作流_1980605758687629313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVSR-SeedVR2-Wan2_2Detailer 视频放大细节增强工作流_1980605758687629313.json
hash: fa6dda0af19210f2
coverage: 0.836364
learned_at: 2026-11-14 00:27:01
nodes: [WanVideoSampler, MarkdownNote, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, Reroute, CLIPTextEncode, CLIPTextEncode, VAEDecode, ModelSamplingSD3, ContextWindowsManual, WanVideoEnhanceAVideoKJ, LayerUtility: PurgeVRAM, VHS_LoadVideo, Note, Note, WanVideoTextEncode, VAELoader, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate, LayerUtility: PurgeVRAM, Note, UNETLoader, TorchCompileModel, PathchSageAttentionKJ, LoraLoaderModelOnly, Reroute, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, SeedVR2, WanVideoBlockSwap, WanVideoTorchCompileSettings, Note, VHS_VideoCombine, LayerUtility: PurgeVRAM, ImageConcatMulti, SeedVR2BlockSwap, VHS_VideoCombine, Note, WanVideoExtraModelSelect, CLIPLoader, LoadWanVideoT5TextEncoder, ImageResizeKJv2, WanVideoFlashVSRDecoderLoader, WanVideoAddFlashVSRInput, WanVideoEmptyEmbeds, VHS_VideoCombine, VAEEncode, ImageResizeKJv2, Int, WanVideoModelLoader, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 888, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FlashVSR-SeedVR2-Wan2_2Detailer 视频放大细节增强工作流_1980605758687629313.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVSR-SeedVR2-Wan2_2Detailer 视频放大细节增强工作流_1980605758687629313.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ContextWindowsManual`
- `WanVideoEnhanceAVideoKJ`
- `LayerUtility: PurgeVRAM`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `Note`
- `UNETLoader` ★核心
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `ImageConcatMulti`
- `SeedVR2BlockSwap`
- `VHS_VideoCombine`
- `Note`
- `WanVideoExtraModelSelect`
- `CLIPLoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoAddFlashVSRInput`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `Int`
- `WanVideoModelLoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `888`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`WanVideoSampler`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`ContextWindowsManual`、`WanVideoEnhanceAVideoKJ`、`LayerUtility: PurgeVRAM`、`VHS_LoadVideo`、`WanVideoTextEncode`、`VAELoader`、`ImageConcanate`、`UNETLoader`、`TorchCompileModel`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`SeedVR2`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`SeedVR2BlockSwap`、`WanVideoExtraModelSelect`、`CLIPLoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoFlashVSRDecoderLoader`、`WanVideoAddFlashVSRInput`、`WanVideoEmptyEmbeds`、`VAEEncode`、`Int`、`WanVideoModelLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、SeedVR2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
