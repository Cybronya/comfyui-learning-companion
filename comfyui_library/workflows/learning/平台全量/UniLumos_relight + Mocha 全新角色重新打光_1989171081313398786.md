---
key: 平台全量/UniLumos_relight + Mocha 全新角色重新打光_1989171081313398786.json
name: UniLumos_relight + Mocha 全新角色重新打光_1989171081313398786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/UniLumos_relight + Mocha 全新角色重新打光_1989171081313398786.json
hash: 438c2b0f8b278fe0
coverage: 0.741176
learned_at: 2026-11-14 01:02:03
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, VHS_VideoCombine, MarkdownNote, WanVideoTextEncode, ImageResizeKJv2, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, WanVideoUniLumosEmbeds, WanVideoEncode, TransparentBGSession+, ImageRemoveBackground+, ImageResizeKJv2, WanVideoEncode, DrawMaskOnImage, InvertMask, WanVideoSetLoRAs, DrawGaussianNoiseOnImage, MarkdownNote, ImageConcatMulti, Note, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, DrawMaskOnImage, MaskFromBatch+, ImageFromBatch+, Reroute, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, SetNode, SetNode, RMBG, CFGNorm, VAELoader, CLIPLoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAEDecode, ImageScaleToTotalPixels, PreviewImage, SetNode, SetNode, SetNode, SetNode, KSampler, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, LayerUtility: PurgeVRAM, PreviewImage, RMBG, MochaEmbeds, WanVideoDecode, WanVideoVAELoader, GetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, Note, WanVideoTextEncode, PreviewImage, Reroute, ImageFromBatch+, GetNode, Reroute, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, VHS_LoadVideo, VHS_LoadVideo, INTConstant, WanVideoLoraSelect, WanVideoModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VHS_VideoCombine, WanVideoSampler, AILab_QwenVL_Advanced, ShowText|pysssss]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 599922074096577, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/UniLumos_relight + Mocha 全新角色重新打光_1989171081313398786.json

> 来源文件 `comfyui_library/workflows/平台全量/UniLumos_relight + Mocha 全新角色重新打光_1989171081313398786.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoUniLumosEmbeds`
- `WanVideoEncode`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `DrawMaskOnImage`
- `InvertMask`
- `WanVideoSetLoRAs`
- `DrawGaussianNoiseOnImage`
- `MarkdownNote`
- `ImageConcatMulti`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `DrawMaskOnImage`
- `MaskFromBatch+`
- `ImageFromBatch+`
- `Reroute`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `RMBG`
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `RMBG`
- `MochaEmbeds`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoTextEncode`
- `PreviewImage`
- `Reroute`
- `ImageFromBatch+`
- `GetNode`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `AILab_QwenVL_Advanced`
- `ShowText|pysssss`

## 关键参数

- `seed` = `599922074096577`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **74%**（63/85）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`ImageResizeKJv2`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoUniLumosEmbeds`、`WanVideoEncode`、`TransparentBGSession+`、`ImageRemoveBackground+`、`DrawMaskOnImage`、`InvertMask`、`WanVideoSetLoRAs`、`DrawGaussianNoiseOnImage`、`MaskFromBatch+`、`ImageFromBatch+`、`RMBG`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`ImageScaleToTotalPixels`、`KSampler`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM`、`MochaEmbeds`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`INTConstant`、`LoraLoaderModelOnly`、`UNETLoader`、`AILab_QwenVL_Advanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、CFGNorm、WanVideoSampler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
