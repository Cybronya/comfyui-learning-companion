---
key: 视频生成/图生视频/小孩工作wan2.1_1964871069591064577.json
name: 小孩工作wan2.1_1964871069591064577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964871069591064577.json
hash: a9a6862b827371a5
coverage: 0.875
learned_at: 2026-10-15 22:31:35
nodes: [WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoVAELoader, CFGNorm, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, SetNode, ImageResizeKJv2, WanVideoSampler, WanVideoSLG, LoadWanVideoT5TextEncoder, ShowText|pysssss, WanVideoLoraSelect, VAEDecode, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEdit, Reroute, Seed (rgthree), EmptyLatentImage, Seed (rgthree), WanVideoTextEncode, VHS_VideoCombine, CR Prompt Text, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, CR Prompt Text, LoadImage, TextEncodeQwenImageEdit, KSampler, Note, LayerUtility: Gemini, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 362000921346101, "steps": 4, "width": 888}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/小孩工作wan2.1_1964871069591064577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964871069591064577.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（40 个）：
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `WanVideoLoraSelect`
- `VAEDecode` ★核心
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEdit`
- `Reroute`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `CR Prompt Text`
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `Note`
- `LayerUtility: Gemini`
- `easy showAnything`

## 关键参数

- `width` = `888`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `362000921346101`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`WanVideoDecode`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoSLG`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`VAEDecode`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEdit`、`Seed (rgthree)`、`EmptyLatentImage`、`WanVideoTextEncode`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoModelLoader`、`LoadImage`、`KSampler`、`LayerUtility: Gemini`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
