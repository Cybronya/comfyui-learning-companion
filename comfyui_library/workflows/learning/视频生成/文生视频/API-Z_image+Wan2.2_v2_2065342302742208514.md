---
key: 视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json
name: API-Z_image+Wan2.2_v2_2065342302742208514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/API-Z_image+Wan2.2_v2_2065342302742208514.json
hash: 63607b2ccd38172b
coverage: 0.804878
learned_at: 2026-10-11 20:21:23
nodes: [CLIPTextEncode, EmptySD3LatentImage, Int, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, WanVideoSampler, VAEDecode, ImageResize+, WanVideoTextEncode, CLIPLoader, UNETLoader, VAELoader, KSampler, Int, VHS_VideoCombine, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, CLIPTextEncode, Int]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, ImageResize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 432307521137100, "steps": 9}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
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

覆盖率 **80%**（33/41）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`Int`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`VAEDecode`、`WanVideoTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSampler`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoDecode`

**缺卡**（7）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanVideoSampler、CreateCFGScheduleFloatList

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
