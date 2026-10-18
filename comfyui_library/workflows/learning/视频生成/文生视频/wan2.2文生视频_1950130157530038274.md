---
key: 视频生成/文生视频/wan2.2文生视频_1950130157530038274.json
name: wan2.2文生视频_1950130157530038274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_1950130157530038274.json
hash: 360d6be3b2b6c107
coverage: 1
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoSetLoRAs, INTConstant, WanVideoSampler, WanVideoDecode, WanVideoSetLoRAs, WanVideoSampler, INTConstant, GetImageSizeAndCount, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, EmptyHunyuanLatentVideo, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoEmptyEmbeds, WanVideoEmptyEmbeds, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频_1950130157530038274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950130157530038274.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `INTConstant`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `EmptyHunyuanLatentVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoEmptyEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`EmptyHunyuanLatentVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、EmptyHunyuanLatentVideo、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
