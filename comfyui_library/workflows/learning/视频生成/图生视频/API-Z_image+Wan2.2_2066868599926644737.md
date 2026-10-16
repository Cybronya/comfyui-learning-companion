---
key: 视频生成/图生视频/API-Z_image+Wan2.2_2066868599926644737.json
name: API-Z_image+Wan2.2_2066868599926644737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066868599926644737.json
hash: 1b564b52875552bb
coverage: 0.975
learned_at: 2026-10-15 22:39:54
nodes: [EmptySD3LatentImage, Int, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, WanVideoSampler, ImageResize+, WanVideoTextEncode, CLIPLoader, VAELoader, VHS_VideoCombine, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, UNETLoader, Int, CLIPTextEncode, KSampler, VAEDecode, WanVideoBlockSwap, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 980898746381468, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/API-Z_image+Wan2.2_2066868599926644737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066868599926644737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `EmptySD3LatentImage`
- `Int`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `ImageResize+`
- `WanVideoTextEncode`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `UNETLoader` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `WanVideoBlockSwap`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `980898746381468`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`EmptySD3LatentImage`、`Int`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`SimpleMath+`、`ImageResize+`、`WanVideoTextEncode`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`WanVideoDecode`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler、CreateCFGScheduleFloatList

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
