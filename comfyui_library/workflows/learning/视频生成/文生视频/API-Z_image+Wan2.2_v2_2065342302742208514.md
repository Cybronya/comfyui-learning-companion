---
key: 视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json
name: API-Z_image+Wan2.2_v2_2065342302742208514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json
hash: 63607b2ccd38172b
coverage: 0.97561
learned_at: 2026-10-15 22:44:01
nodes: [CLIPTextEncode, EmptySD3LatentImage, Int, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, WanVideoSampler, VAEDecode, ImageResize+, WanVideoTextEncode, CLIPLoader, UNETLoader, VAELoader, KSampler, Int, VHS_VideoCombine, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, CLIPTextEncode, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 432307521137100, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
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
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `VAEDecode` ★核心
- `ImageResize+`
- `WanVideoTextEncode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `Int`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `CLIPTextEncode` ★核心
- `Int`

## 关键参数

- `seed` = `432307521137100`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`Int`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`SimpleMath+`、`VAEDecode`、`ImageResize+`、`WanVideoTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSampler`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`WanVideoDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler、CreateCFGScheduleFloatList

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
