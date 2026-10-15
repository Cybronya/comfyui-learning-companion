---
key: 图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json
name: flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json
hash: d1cf0b3d4e5b3bf4
coverage: 0.918919
learned_at: 2026-10-15 22:27:43
nodes: [WanVideoExperimentalArgs, WanVideoSLG, VAELoader, FluxKontextImageScale, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, CLIPTextEncode, KSampler, VAEEncode, ReferenceLatent, FluxGuidance, EmptySD3LatentImage, ConditioningZeroOut, WanVideoBlockSwap, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoDecode, LayerUtility: PurgeVRAM V2, UNETLoader, DualCLIPLoader, LoadImage, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, PreviewImage, VAEDecode, SetNode, GetNode, WanVideoImageToVideoEncode, WanVideoTextEncode, Power Lora Loader (rgthree), WanVideoEnhanceAVideo, WanVideoSampler, WanVideoFreeInitArgs, VHS_VideoCombine]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 885189490893767, "steps": 10}
---

# 图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `VAELoader`
- `FluxKontextImageScale`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `Power Lora Loader (rgthree)`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoFreeInitArgs`
- `VHS_VideoCombine`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `885189490893767`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoSLG`、`VAELoader`、`FluxKontextImageScale`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJv2`、`CLIPTextEncode`、`KSampler`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`VAEDecode`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`Power Lora Loader (rgthree)`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoFreeInitArgs`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
