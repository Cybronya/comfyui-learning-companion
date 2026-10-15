---
key: 视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json
name: API-Z_image+Wan2.2_2058887604485058562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json
hash: 6108337d5b1ec901
coverage: 0.975
learned_at: 2026-10-15 22:44:01
nodes: [Int, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, ImageResize+, WanVideoTextEncode, VAELoader, VHS_VideoCombine, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, WanVideoSampler, WanVideoSampler, Int, UNETLoader, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, EmptySD3LatentImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 30287761845469, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/API-Z_image+Wan2.2_2058887604485058562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `Int`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
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
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResize+`
- `WanVideoTextEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Int`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `30287761845469`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`Int`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`SimpleMath+`、`ImageResize+`、`WanVideoTextEncode`、`VAELoader`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoSampler`、`UNETLoader`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`EmptySD3LatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler、CreateCFGScheduleFloatList

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
