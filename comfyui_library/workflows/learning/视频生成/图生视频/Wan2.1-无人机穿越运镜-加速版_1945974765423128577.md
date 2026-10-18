---
key: 视频生成/图生视频/Wan2.1-无人机穿越运镜-加速版_1945974765423128577.json
name: Wan2.1-无人机穿越运镜-加速版_1945974765423128577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-无人机穿越运镜-加速版_1945974765423128577.json
hash: 7ca811d848accfa0
coverage: 0.875
learned_at: 2026-10-15 22:30:43
nodes: [VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPVisionLoader, ModelSamplingSD3, VAEDecode, TextBox, ttN concat, WanImageToVideo, KSampler, RH_LLMAPI_NODE, easy showAnything, DeepTranslatorTextNode, easy showAnything, CLIPVisionEncode, LayerUtility: PurgeVRAM V2, WanVideoBlockSwap, LoadImage, Int, DF_Image_scale_to_side, PreviewImage, ImageResizeKJ, PreviewImage, Get Image Size, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, LayerUtility: PurgeVRAM V2, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoSampler, VHS_VideoCombine, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 334, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.1-无人机穿越运镜-加速版_1945974765423128577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1945974765423128577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `TextBox`
- `ttN concat`
- `WanImageToVideo`
- `KSampler` ★核心
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `DeepTranslatorTextNode`
- `easy showAnything`
- `CLIPVisionEncode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoBlockSwap`
- `LoadImage`
- `Int`
- `DF_Image_scale_to_side`
- `PreviewImage`
- `ImageResizeKJ`
- `PreviewImage`
- `Get Image Size`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `334`
- `steps` = `4`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`ModelSamplingSD3`、`VAEDecode`、`TextBox`、`ttN concat`、`WanImageToVideo`、`KSampler`、`RH_LLMAPI_NODE`、`DeepTranslatorTextNode`、`CLIPVisionEncode`、`LayerUtility: PurgeVRAM V2`、`WanVideoBlockSwap`、`LoadImage`、`Int`、`DF_Image_scale_to_side`、`ImageResizeKJ`、`Get Image Size`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
