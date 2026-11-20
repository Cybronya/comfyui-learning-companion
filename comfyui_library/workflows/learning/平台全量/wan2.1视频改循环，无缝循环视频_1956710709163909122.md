---
key: 平台全量/wan2.1视频改循环，无缝循环视频_1956710709163909122.json
name: wan2.1视频改循环，无缝循环视频_1956710709163909122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1视频改循环，无缝循环视频_1956710709163909122.json
hash: a11d13955edb1450
coverage: 0.666667
learned_at: 2026-11-14 01:19:14
nodes: [WanVideoNAG, TorchCompileModelWanVideoV2, WanVideoEnhanceAVideoKJ, TrimVideoLatent, WanVaceToVideo, ModelSamplingSD3, VAEDecode, easy cleanGpuUsed, CrossFadeImages, CrossFadeImages, VHS_SplitImages, VHS_SplitImages, VHS_SplitImages, SetNode, SetNode, GetNode, GetNode, easy mathInt, GetImageSize+, easy mathInt, SetNode, SetNode, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, GetNode, PrimitiveInt, PrimitiveInt, MarkdownNote, VHS_LoadVideoPath, LoraLoaderModelOnly, VAELoader, CLIPLoaderGGUF, UNETLoader, CLIPLoader, KSampler, WanVideoVACEStartToEndFrame, PreviewImage, VHS_VideoCombine, PrimitiveStringMultiline, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 43, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.1视频改循环，无缝循环视频_1956710709163909122.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1视频改循环，无缝循环视频_1956710709163909122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `WanVideoNAG`
- `TorchCompileModelWanVideoV2`
- `WanVideoEnhanceAVideoKJ`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CrossFadeImages`
- `CrossFadeImages`
- `VHS_SplitImages`
- `VHS_SplitImages`
- `VHS_SplitImages`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetImageSize+`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `VHS_LoadVideoPath`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoaderGGUF`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `43`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`WanVideoNAG`、`TorchCompileModelWanVideoV2`、`WanVideoEnhanceAVideoKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`ModelSamplingSD3`、`VAEDecode`、`easy cleanGpuUsed`、`CrossFadeImages`、`VHS_SplitImages`、`easy mathInt`、`GetImageSize+`、`CLIPTextEncode`、`VHS_LoadVideoPath`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoaderGGUF`、`UNETLoader`、`CLIPLoader`、`KSampler`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、TrimVideoLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
